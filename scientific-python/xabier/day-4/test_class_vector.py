import pytest
from class_vector import Vector

@pytest.mark.parametrize("u, v", [(Vector([1,2]), Vector([3,4])), (Vector([5,6]), Vector([7, 8]))])
def test_class_vector(u, v):
    assert u + v == v + u
    assert v - v == 0
    assert 2 * u == u + u
    assert abs(v)**2 == pytest.approx(v.dot(v))

def test_different_dimension():
    u = Vector([1,2])
    v = Vector([3,4,5])
    with pytest.raises(ValueError):
        u + v
