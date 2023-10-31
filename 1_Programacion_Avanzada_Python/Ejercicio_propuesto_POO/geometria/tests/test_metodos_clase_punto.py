import pytest
from geom2d.punto import Punto
from geom2d.vector import Vector

# Pruebas para el método 'distance'
def test_distance():
    punto1 = Punto(1, 2)
    punto2 = Punto(3, 3)
    distancia = punto1.distance(punto2)
    assert distancia == 2.23606797749979

# Pruebas para el método 'resta'
def test_resta():
    punto1 = Punto(1, 2)
    punto2 = Punto(3, 3)
    resultado = punto2 - punto1
    assert resultado == Vector(2, 1)
