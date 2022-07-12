import pytest

from samples import measures

def test_baseunit():
    M = measures.M
    assert M.value == 1.
    assert M.mark == 'm'

    M3 = measures.M3
    assert M3.value == 1.
    assert M3.mark == 'm^3.0'

    kg = measures.kg
    assert kg.value == 1.
    assert kg.mark == 'kg'

    s = measures.s
    assert s.value == 1.
    assert s.mark == 's'

    s2 = measures.s2
    assert s2.value == 1.
    assert s2.mark == 's^2.0'

    kg_s2 = measures.kg_s2
    assert kg_s2.value == 1.
    assert kg_s2.mark == 'kg*s^2.0'

    grav = measures.grav
    assert grav.value == 1.
    assert grav.mark == '(m^3.0)/(kg*s^2.0)'