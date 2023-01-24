"""
A suite of general-purpose functions used in this pipeline.
"""

from gzip import open as gzip_open
from io import StringIO
from os import makedirs
from os.path import exists, join
from typing import Generator

from numpy import nan
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.table import Table, TableStyleInfo
from pandas import DataFrame, ExcelWriter, Series, read_csv

# %%

############################################################
############ DEFINE GENRAL-PURPOSE CALCULATIONS ############
############################################################
def merge(input_row: set) -> str:
    """Generate row value to save in df
    Args:
        value (set): The set you wish to convert
    Returns:
        str: The converted value, ready to store.
    """
    row_value_as_list = list(input_row)
    if len(row_value_as_list) == 1:
        return str(row_value_as_list[0])
    else:
        return " | ".join(input_row)


def chunk(input_data: DataFrame, size: int) -> Generator:
    """Renders a generator to yield chunks of data from the original file.
    Args:
        dataset (pd.DataFrame): The dataset to divide into chunks.
        size (int): The maximum size of the resulting chunks.
    Returns:
        [type]: [description]
    Yields:
        Generator: [description]
    """
    return (input_data[pos : pos + size] for pos in range(0, len(input_data), size))


def generate_notation(input_row: Series, gene_strand: str) -> str:
    """
    Parses a row and returns the HGVS notation to query E! Ensembl.

    Args:
        row (Series): A row (generated from .iterrows() method) for which notation is needed.
    Returns:
        str: HGVS notation for the given variant row.
    """
    alleles = input_row["ALT"].split(",")
    notation = list()
    for allele in alleles:
        if (len(input_row["REF"]) > len(allele)) | (
            len(input_row["REF"]) == len(allele)
        ):
            stop_coordinates = int(input_row["POS"]) + (len(input_row["REF"]) - 1)
            notation.append(
                f"{input_row['CHROM']}:{input_row['POS']}-{stop_coordinates}:1/{allele}"
            )
        elif len(input_row["REF"]) < len(allele):
            stop_coordinates = int(input_row["POS"]) + len(input_row["REF"])
            notation.append(
                f"{input_row['CHROM']}:{input_row['POS']}-{stop_coordinates}:{gene_strand}/{allele}"
            )
        return notation


def read_vcf(path: str) -> DataFrame:
    """
    Function to import a VCF file as a Pandas dataframe. Does not include Genotype columns.
    CREDIT: https://gist.github.com/dceoy/99d976a2c01e7f0ba1c813778f9db744

    Args:
        path (str): Path to the VCF file in question
    Returns:
        Dataframe: A Pandas Dataframe of the VCF files content.
    """
    with gzip_open(path, "rt") as file:
        lines = [l for l in file if not l.startswith("##")]
    return read_csv(
        StringIO("".join(lines)),
        dtype={
            "#CHROM": str,
            "POS": int,
            "ID": str,
            "REF": str,
            "ALT": str,
            "QUAL": str,
            "FILTER": str,
            "INFO": str,
        },
        sep="\t",
    ).rename(columns={"#CHROM": "CHROM"})


def calculate_frequency(alternate_allele_count: int, total_count: int) -> int:
    """Calculate percentage frequency for alleles based on count data.
    Args:
        alt (int): Number of observations of the alternate allele.
        total (int): Total number of observations of any allele.
    Returns:
        int: decimal percentage allele frequency.
    """
    if alternate_allele_count != 0 and total_count == 0:
        raise Exception("The total_count cannot be zero.")
    if alternate_allele_count == 0 and total_count == 0:
        return nan
    return alternate_allele_count / total_count


def generate_params(transcription_ids: list, canonical=False) -> dict:
    """
    Returns generated parameters suitable for the E! Ensembl VEP tool API.

    Args:
        transcription_ids (list): A list of transcript IDs to filter for.
        canonical (bool, optional): Only consider canonical transcripts. Defaults to False.

    Returns:
        dict: A dictionary of parameters suitable for the VEP API.
    """
    params = {
        "hgvs": True,
        "CADD": True,
        "Phenotypes": True,
        "domains": True,
        "canonical": canonical,
        "refseq": True,
        "LoF": True,
        "dbNSFP": "SIFT4G_score,SIFT4G_pred,Polyphen2_HVAR_score,Polyphen2_HVAR_pred",
    }
    if transcription_ids:
        params["transcription_ids"] = transcription_ids
    return params


def directory_exists(path: str):
    """Test weather or not a directory exists. If not, create it.
    Args:
        path (str): file path of the directory to test.
    """
    if not exists(path):
        makedirs(path)


# ToDo: Find better way to type hint exists_behaviour
def save_or_append_to_excel(
    data_to_save: DataFrame,
    cluster: str,
    gene: str,
    sheet_name: str,
    exists_behaviour: str,
):
    """
    A small function that writes or appends to an Excel file depending on if it exists or not.

    Args:
        data_to_save (DataFrame): A Pandas DataFrame to save to Excel format.
        cluster (str): The cluster level being saved.
        gene (str): The gene being saved.
    """
    path = join(
        "..",
        "..",
        "results",
        "FINAL",
        f"{cluster}-{gene}.xlsx",
    )
    if exists(path):
        mode = "a"
    else:
        mode = "w"
    kwargs = {"engine": "openpyxl", "mode": mode}
    if exists_behaviour and mode == "a":
        kwargs["if_sheet_exists"] = exists_behaviour
    with ExcelWriter(  # pylint: disable=abstract-class-instantiated
        path, **kwargs
    ) as writer:
        data_to_save.to_excel(
            writer,
            index=False,
            sheet_name=sheet_name,
        )
        worksheet = writer.sheets[sheet_name]
        (row_count, column_count) = data_to_save.shape

        # Define the table using the OpenPyExel engine:
        table = Table(
            ref=f"A1:{get_column_letter(column_count)}{row_count+1}",
            displayName=sheet_name,
        )

        # Add a nice style, because I like nice-looking tables!
        # Add a default style with striped rows and banded columns
        style = TableStyleInfo(
            name="TableStyleMedium9",
            showFirstColumn=False,
            showLastColumn=False,
            showRowStripes=True,
            showColumnStripes=True,
        )
        table.tableStyleInfo = style

        # Add an Excel table to the data:
        worksheet.add_table(table)


# %%
