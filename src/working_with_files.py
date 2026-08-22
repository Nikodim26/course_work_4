from abc import ABC, abstractmethod
from pathlib import Path


class Working_With_Files(ABC):

    def __init__(self, file, data):
        self.file = file
        self.data = data

    @abstractmethod
    def write_file(self):
        pass

    @abstractmethod
    def write_file_add(self,*args):
        pass