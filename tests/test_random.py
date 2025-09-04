import pytest
from random import randint


@pytest.mark.benchmark
def test_random(benchmark):
    @benchmark
    def _():
        loops = randint(0, 1000)
        for _ in range(loops):
            a = 2
            b = a
            a = b
