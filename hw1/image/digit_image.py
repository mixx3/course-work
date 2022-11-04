from .base import Image
from .utils import normalize_vector, check_correlation
import numpy as np


class DigitImage(Image):
    def __init__(self, vector: np.ndarray):
        self.vector = vector
        self.is_normalized: bool = False

    def normalize(self):
        self.vector = normalize_vector(self.vector)
        self.is_normalized = True
        return self

    def check_correlation(self, other: Image) -> float:
        return check_correlation(self.vector, other.vector)
