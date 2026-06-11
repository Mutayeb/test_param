import pytest

def second_largest(arr):
    """
    Python implementation mimicking the exact logic and edge-case
    handling (-1 returns) of the original C++ function.
    """
    # Using 32-bit INT_MIN to match C++ behavior
    INT_MIN = -2147483648
    largest = INT_MIN
    second = INT_MIN

    for num in arr:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    return -1 if second == INT_MIN else second


@pytest.mark.parametrize(
    "arr, expected",
    [
        # Normal case
        ([12, 35, 1, 10, 34, 1], 34),
        # Largest appears multiple times
        ([10, 20, 20, 5], 10),
        # Second largest appears multiple times
        ([10, 8, 8, 5], 8),
        # Sorted ascending
        ([1, 2, 3, 4, 5], 4),
        # Sorted descending
        ([5, 4, 3, 2, 1], 4),
        # Negative numbers
        ([-5, -2, -10, -1], -2),
        # Two elements
        ([10, 5], 5),
        # All elements equal
        ([7, 7, 7, 7], -1),
        # Single element
        ([5], -1),
        # Empty array
        ([], -1),
        # Second largest repeated
        ([100, 90, 90, 80], 90),
        # Largest repeated many times
        ([100, 100, 100, 90], 90),
    ],
)
def test_Solution(arr, expected):
    assert second_largest(arr) == expected