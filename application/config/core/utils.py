import enum
from uuid import uuid4
from pathlib import Path

# Create yours utils here.


class CALLBACK(enum.Enum):
    FOLDER = 0
    NAME = 1
    EXT = 2


def get_path(instance, filename, callback=None):
    file_path = Path(filename)
    folder_path = file_path.parent
    suffix = file_path.suffix
    name = f'{uuid4()}{suffix}'

    if callback is CALLBACK.FOLDER:
        return str(folder_path / name)
    elif callback is CALLBACK.NAME:
        return file_path.name
    elif callback is CALLBACK.EXT:
        return suffix
    else:
        return name
