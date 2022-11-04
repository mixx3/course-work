import numpy as np


def normalize_vector(v: np.ndarray):
    return v / np.sqrt(np.dot(v, v))


def check_correlation(g: np.ndarray, f: np.ndarray) -> float:
    return np.dot(f, g) / np.sqrt(np.dot(f, f) * np.dot(g, g))
