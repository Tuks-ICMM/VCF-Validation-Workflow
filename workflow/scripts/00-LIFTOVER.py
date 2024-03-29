#!/usr/bin/env python
"""A Python script designed to calculate frequencies, FishersExact and Variant Effect Predictions.
"""


import os
from os.path import join

from pandas import read_csv
from snakemake import shell

__author__ = "Graeme Ford"
__credits__ = [
    "Graeme Ford",
    "Prof. Michael S. Pepper",
    "Prof. Fourie Joubert",
    "Antionette Colic",
    "Fatima Barmania",
    "Megan Ryder",
]
__version__ = "1.0.0"
__maintainer__ = "Graeme Ford"
__email__ = "graeme.ford@tuks.co.za"
__status__ = "Development"


# Define constant:
config = snakemake.config
wildcards = snakemake.wildcards
params = snakemake.params
datasets = read_csv(join("input", "datasets.csv"))


# Define functions:
def directoryExists(path: str):
    """Test weather or not a directory exists. If not, create it.

    Args:
        path (str): file path of the directory to test.
    """
    if not os.path.exists(path):
        os.makedirs(path)


print("Determining Liftover requirements now...")
listed_refs: list = datasets.loc[
    datasets["dataset_name"] == wildcards.dataset, "reference_genome"
].item()
if listed_refs != "GRCh38":
    shell(
        "echo 'Liftover required. All datasets have been mapped to {}'".format(
            listed_refs
        )
    ),
    shell("module load liftover"),
    if listed_refs == "GRCh37" or listed_refs == "Hg19":
        shell("echo 'Lifting from GRCh37 to GRCh38.'"),
        directoryExists("results/LIFTOVER"),
        shell(
            "plink2 --vcf results/PREP/{wildcards.dataset}.vcf.gz --set-all-var-ids @:#\$r-\$a --allow-extra-chr --new-id-max-allele-len 40 truncate --chr 1-22 --out results/LIFTOVER/{wildcards.dataset}_PREP --export vcf-4.2 bgz --output-chr chr26"
        ),
        shell(
            "sleep 60; tabix -p vcf results/LIFTOVER/{wildcards.dataset}_PREP.vcf.gz"
        ),
        shell(
            "picard-tools LiftoverVcf I=results/LIFTOVER/{wildcards.dataset}_PREP.vcf.gz O=results/LIFTOVER/{wildcards.dataset}_LIFTOVER.vcf.gz C={params.chainFile} REJECT=results/LIFTOVER/{wildcards.dataset}_REJECTED.vcf.gz R={params.ref}"
        ),
        shell(
            "bcftools sort -m 1G -T results/LIFTOVER -O z -o results/LIFTOVER/{wildcards.dataset}.vcf.gz results/LIFTOVER/{wildcards.dataset}_LIFTOVER.vcf.gz"
        ),
    # TODO: Add conditionals for other human reference genome builds
    else:
        print(
            "No liftover required. Dataset {} is already mapped to GRCh38.".format(
                wildcards.dataset
            )
        ),
        shell("touch results/LIFTOVER/{wildcards.dataset}_EXCLUDE.dat"),
        shell(
            "plink --map input/{wildcards.dataset}.map --ped input/{wildcards.dataset}.ped --allow-extra-chr --chr 1-22 --recode vcf --keep-allele-order --exclude {params.exclusionList} --out results/LIFTOVER/{wildcards.dataset}"
        ),
    # shell("bgzip results/LIFTOVER/{wildcards.dataset}.vcf"),
    shell("sleep 1m; tabix -f -p vcf results/LIFTOVER/{wildcards.dataset}.vcf.gz"),
    shell(
        "echo 'results/LIFTOVER/{wildcards.dataset}.vcf.gz' >> results/LIFTOVER/merge.list"
    )
else:
    shell(
        "plink2 --vcf results/PREP/{wildcards.dataset}.vcf.gz --set-all-var-ids @:#\$r-\$a --allow-extra-chr --new-id-max-allele-len 400 truncate --chr 1-22 --out results/LIFTOVER/{wildcards.dataset} --export vcf-4.2 bgz --output-chr chr26"
    ),
    shell("sleep 60; tabix -p vcf results/LIFTOVER/{wildcards.dataset}.vcf.gz"),
    shell(
        "echo 'results/LIFTOVER/{wildcards.dataset}.vcf.gz' >> results/LIFTOVER/merge.list"
    )
