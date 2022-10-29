from abc import ABC, abstractmethod
from os import path
from random import shuffle, seed
from . import WeightSet, WeightStream


class DatasetReader(ABC):

    def offline(self) -> WeightSet:
        '''Return a WeightSet to support an offline algorithm'''
        (capacity, weights) = self._load_data_from_disk()
        seed(42)          # always produce the same shuffled result
        shuffle(weights)  # side effect shuffling
        return (capacity, weights)

    def online(self) -> WeightStream:
        '''Return a WeighStream, to support an online algorithm'''
        (capacity, weights) = self.offline()

        def iterator():  # Wrapping the contents into an iterator
            for w in weights:
                yield w  # yields the current value and moves to the next one

        return (capacity, iterator())

    @abstractmethod
    def _load_data_from_disk(self) -> WeightSet:
        '''Method that read the data from disk, depending on the file format'''
        pass


class BinppReader(DatasetReader):
    '''Read problem description according to the BinPP format'''

    def __init__(self, filename: str) -> None:
        if not path.exists(filename):
            raise ValueError(f'Unknown file [{filename}]')
        self.__filename = filename

    def _load_data_from_disk(self) -> WeightSet:
        with open(self.__filename, 'r') as reader:
            nb_objects: int = int(reader.readline())
            capacity: int = int(reader.readline())
            weights = []
            for _ in range(nb_objects):
                weights.append(int(reader.readline()))
            return (capacity, weights)


class JburkardtReader(DatasetReader):

    def __init__(self, filename: str) -> None:
        if not path.exists(filename):
            raise ValueError(f'Unknown file [{filename}]')
        self.__filename = filename

    def _load_data_from_disk(self) -> WeightSet:        
        filenameLocation = self.__filename
        
        with open(self.__filename, 'r') as readerC:
            capacity: int = int(readerC.readline())
        
        filenameLocation = filenameLocation.replace("_c", "_s")

        with open(filenameLocation, 'r') as readerS:
            numberOfObjects = \
                [int(l) for l in (line.strip() for line in readerS) if l]
            nb_objects: int = int(len(numberOfObjects))
        
        filenameLocation = filenameLocation.replace("_s", "_w")

        with open(filenameLocation, 'r') as readerW:
            weights = [int(l) for l in (line.strip() for line in readerW) if l]

        return (capacity, weights)     
