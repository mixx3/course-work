import pytest
import numpy as np
from sklearn.datasets import load_digits


@pytest.fixture(scope="session")
def data_sample() -> np.ndarray:
    yield load_digits().data


