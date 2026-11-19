
import pytest
from src.parcel_acceptance import is_parcel_accepted


# Test valid and rejected parcels
@pytest.mark.parametrize("weight, length, expected", [
    (1000, 100, True),
    (1, 1, True),
    (20000, 100, True),
    (20000, 200, True),
    (0, 100, False),
    (1000, 0, False),
    (20001, 100, False),
    (1000, 201, False),
])
def test_parcel_acceptance_returns_expected_result(
    weight, length, expected
):
    # Arrange
    # Inputs and expected result are provided by parametrize

    # Act
    result = is_parcel_accepted(weight, length)

    # Assert
    assert result is expected


# Test invalid parcel inputs
@pytest.mark.parametrize("weight, length, error", [
    (-1, 100, ValueError),
    (1000, -1, ValueError),
    (1000.5, 100, TypeError),
    (1000, "100", TypeError),
    (True, 100, TypeError),
])
def test_parcel_acceptance_raises_expected_error(
    weight, length, error
):
    # Arrange
    # Inputs and error are provided by parametrize

    # Act & Assert
    with pytest.raises(error):
        is_parcel_accepted(weight, length)
