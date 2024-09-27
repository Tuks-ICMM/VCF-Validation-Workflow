from os.path import exists, join
from os import makedirs
from typing import Union


def directoryExists(path: str):
    """Test weather or not a directory exists. If not, create it.

    Args:
        path (str): file path of the directory to test.
    """
    if not exists(path):
        makedirs(path)

def outputDir(path: str) -> str:
    """This function consults the `config.json` file to determine if a pre-set output directory has been specified. If it has, the provided directory will be used. If not, the current working directory will be used."""
    if "output-dir" in config:
        OUTPUT_DIR_PATH = join(*config["output-dir"])
        return join(OUTPUT_DIR_PATH, path)
    else:
        return join("results", path)