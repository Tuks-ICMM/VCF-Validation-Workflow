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

def out(path: str) -> str:
    """This function consults the `manifest.json` file and uses the provided directory."""
    if "output" in config:
        OUTPUT_DIR_PATH = join(*config["output"])
        return join(OUTPUT_DIR_PATH, path)
    else:
        return join("results", path)