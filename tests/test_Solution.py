import subprocess
import pytest
import os

EXE_NAME = "solution.exe" if os.name == 'nt' else "solution.out"
RUN_CMD = [f".\\{EXE_NAME}"] if os.name == 'nt' else [f"./{EXE_NAME}"]

@pytest.fixture(scope="session", autouse=True)
def compile_cpp():
    # Compiles cleanly to .exe on Windows or .out on Linux/Mac
    compile_cmd = ["g++", "-O3", "solution.cpp", "-o", EXE_NAME]
    process = subprocess.run(compile_cmd, capture_output=True, text=True)
    if process.returncode != 0:
        raise RuntimeError(f"C++ Compilation failed:\n{process.stderr}")
    yield
    if os.path.exists(EXE_NAME):
        os.remove(EXE_NAME)

import pytest

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
        ([7, 7, 7, 7], None),

        # Single element
        ([5], None),

        # Empty array
        ([], None),

        # Second largest repeated
        ([100, 90, 90, 80], 90),

        # Largest repeated many times
        ([100, 100, 100, 90], 90),
    ]
)
def test_Solution(arr, expected):
    n = len(arr)
    input_data = f"{n}\n" + " ".join(map(str, arr))

    # Uses the correct execution command for Windows vs Linux
    process = subprocess.run(
        RUN_CMD,
        input=input_data,
        capture_output=True,
        text=True,
    )

    assert int(process.stdout.strip()) == expected