from enum import Enum


class ExportFormat(str, Enum):
    DOCKER = "docker"
    WE = "we"
    PEX = "pex"
    ZIP = "zip"
    PYZ = "pyz" # https://github.com/ClericPy/zipapps