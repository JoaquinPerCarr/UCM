import math
from typing import Self


class Vector:
    def __init__(self, x: float, y: float):
        # _x, _y son atributos privados.
        self._x: float = x
        self._y: float = y

        # Adición de una 3a componente para diferenciarla del punto.
        self._z: str = 'v'

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    @property
    def mod(self) -> float:
        return math.sqrt(self.x**2 * self.y**2)

    def __eq__(self, other: Self) -> bool:
        return self.x == other.x and self.y == other.y

    def __le__(self, other: Self) -> bool:
        return self.mod <= other.mod

    # Modificamos el hash, para que tenga la componente 'tipo' y se diferencie del hash de la clase Punto
    def __hash__(self):
        return hash((self.x, self.y))

    def __add__(self, other: Self) -> Self:
        """
        Suma de vectores
        """
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Self) -> Self:
        """
        Resta de vectores
        """
        return Vector(self.x - other.x, self.y - other.y)

    def __neg__(self) -> Self:
        """
        Vector inverso
        """
        return Vector(-self.x, -self.y)

    def __rmul__(self, other: float) -> Self:
        """
        Producto de escalar (real) por vector
        """
        return Vector(other * self.x, other * self.y)

    def __mul__(self, other: Self) -> float:
        """
        Producto escalar de vectores
        """
        return self.x * other.x + self.y * other.y

    def __repr__(self) -> str:
        return f'V({self.x}, {self.y})'

    def __str__(self) -> str:
        return f'({self.x:.4f}, {self.y:.4f})'


def str_vs_repr():
    v = Vector(math.pi/2, math.pi)
    print(f'El vector {v} tiene modulo {v.mod}')
    print(repr(v))


def arithmetic():
    v1 = Vector(1, 0)
    v2 = Vector(0, -1)
    lam = 2.0
    print(f'{v1} + {v2} = {v1 + v2}')
    print(f'{v1} - {v2} = {v1 - v2}')
    print(f'-{v1} = {-v1}')
    print(f'{v1} * {v2} = {v1 * v2}')
    print(f'{lam} * {v1} = {lam * v1}')


def test_hash():
    svector = {Vector(1, 0), Vector(0, 1)}
    print(Vector(1.0, 0.0) == Vector(1, 0), Vector(1.0, 0.0) in svector)
    print(Vector(0, 1.0) == Vector(0, 1), Vector(0, 1.0) in svector)


def comparison():
    pairs = [(Vector(1.0, 1.0), Vector(1.0, 1.0)),
             (Vector(1.0, 0.5), Vector(1.0, 1.0)),
             (Vector(1.0, 1.5), Vector(1.0, 1.0)),
             ]

    for v1, v2 in pairs:
        print(f'{v1}=={v2}: {v1 == v2}')
        print(f'{v1}<={v2}: {v1 <= v2}')

        try:
            print(f'{v1}<{v2}: {v1 < v2}')
        except TypeError as e:
            print(f"excepción capturada: {e}")


"""
def main():
    v = Vector(2.0, 3.0)
    print(f'El vector {v} tiene modulo {v.mod}')
    print(repr(v))

    pairs = [(Vector(1.0, 1.0), Vector(1.0, 1.0)),
             (Vector(1.0, 0.5), Vector(1.0, 1.0)),
             (Vector(1.0, 1.5), Vector(1.0, 1.0)),
             ]

    for v1, v2 in pairs:
        print(f'{v1}=={v2}: {v1==v2}')
        print(f'{v1}<={v2}: {v1<=v2}')

        try:
            print(f'{v1}<{v2}: {v1<v2}')
        except TypeError as e:
            print(f"excepción capturada: {e}")
"""
