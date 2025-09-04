import pytest
from fibonacci import iterative_fibonacci


@pytest.mark.parametrize(
    "n", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
)
@pytest.mark.benchmark
def test_iterative_fibo(n, benchmark):
    @benchmark
    def _():
        iterative_fibonacci(n)
