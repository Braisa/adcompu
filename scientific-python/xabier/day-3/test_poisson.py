import pytest
from numpy import exp
from poisson import poisson

if __name__ == "__main__":
    def test_poisson(mu):
        assert sum(poisson(n, mu) for n in range(0, 51)) == pytest.approx(1)
        assert sum(n*poisson(n, mu) for n in range(0, 51)) == pytest.approx(mu)
        assert poisson(0, mu) == pytest.approx(exp(-mu))

    test_poisson(5)
    print("Test for mu=5 successful!")


@pytest.mark.parametrize("mu", range(0, 11))
def test_poisson(mu):
    assert sum(poisson(n, mu) for n in range(0, 51)) == pytest.approx(1)
    assert sum(n*poisson(n, mu) for n in range(0, 51)) == pytest.approx(mu)
    assert poisson(0, mu) == pytest.approx(exp(-mu))
