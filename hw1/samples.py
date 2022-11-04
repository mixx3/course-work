from sklearn.datasets import load_digits
from image import normalize_vector, check_correlation

digits = load_digits()
sample_digit = 0


def test_check_denormalized(digit: int = sample_digit) -> float:
    num_sample_1 = digits.data[sample_digit]
    num_sample_2 = digits.data[sample_digit + 10]
    return check_correlation(num_sample_1, num_sample_2)


def test_check_normalized(digit: int = sample_digit) -> float:
    num_sample_1 = normalize_vector(digits.data[sample_digit])
    num_sample_2 = normalize_vector(digits.data[sample_digit + 10])
    return check_correlation(num_sample_1, num_sample_2)


if __name__ == "__main__":
    print(type(digits.data))
    print(test_check_normalized())
    print(test_check_denormalized())
