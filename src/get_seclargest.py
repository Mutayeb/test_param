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