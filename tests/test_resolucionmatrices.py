import pytest
import source.resolucionmatrices as resolucion

simplex = [[-7, -3, -4, 0, 0, 0], [2, 3, 3, 1, 0, 172], [4, 7, 2, 0, 1, 125]]

def test_encontrarColPivote():
    result = resolucion.encontrarColPivote(simplex)
    assert result == 0

def test_encontrarfilapivote():
    result = resolucion.encontrarfilapivote(simplex, 0)
    assert result == 2