
import pytest
from src.parcel_fee import delivery_fee


# Test valid parcel weights
@pytest.mark.parametrize("weight, expected", [
    (1, 500),
    (500, 500),
    (1000, 500),
    (1001, 1000),
    (20000, 1000),
])
def test_delivery_fee_returns_expected_fee(weight, expected):
    # Arrange
    # Weight and expected fee are provided by parametrize

    # Act
    result = delivery_fee(weight)

    # Assert
    assert result == expected


# Test invalid parcel weights
@pytest.mark.parametrize("weight, error", [
    (0, ValueError),
    (20001, ValueError),
    (1.5, TypeError),
    ("1000", TypeError),
    (True, TypeError),
])
def test_delivery_fee_raises_expected_error(weight, error):
    # Arrange
    # Weight and error are provided by parametrize

    # Act & Assert
    with pytest.raises(error):
        delivery_fee(weight)
