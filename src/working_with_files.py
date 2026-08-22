from abc import ABC
from pathlib import Path


class Working_With_Files(ABC):

    def __init__(self, file):
        self.path=Path(__file__).resolve().parent.parent / "data" / file

    def write_file(self):
       pass

    def reading_file(self):
       pass