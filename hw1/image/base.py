from abc import ABC, abstractmethod


class Image(ABC):
    @abstractmethod
    def __init__(self):
        self.vector = None
        self.is_normalized = False
        raise NotImplementedError

    @abstractmethod
    def normalize(self):
        raise NotImplementedError

    @abstractmethod
    def check_correlation(self, other):
        raise NotImplementedError
