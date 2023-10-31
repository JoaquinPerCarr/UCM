from geom2d.vector import Vector
import math


class Punto:
    def __init__(self, x: float, y: float):
        self._x: float = x
        self._y: float = y

    @property  # Getter x (Lectura)
    def x(self) -> float:
        return self._x

    @x.setter  # Setter x (Modificación)
    def x(self, value: float):
        self._x = value

    @property  # Getter y
    def y(self) -> float:
        return self._y

    @y.setter  # Setter y
    def y(self, value: float):
        self._y = value

    def __str__(self):
        return f"Punto({self._x}, {self._y})"

    def __repr__(self):
        return f"Punto({self._x}, {self._y})"

    def __hash__(self):
        return hash((self._x, self._y, 'Punto'))

    def __sub__(self, other):
        if isinstance(other, Punto):
            return Vector(self._x - other.x, self._y - other.y)  # Revisar que esto funciona bien
        else:
            raise ValueError("La resta solo esta definida punto a punto.")

    def distance(self, other):
        if isinstance(other, Punto):
            dx = self._x - other.x
            dy = self._y - other.y
            dist = math.sqrt((dx**2 + dy**2))
            return dist
        else:
            raise ValueError("La distancia solo esta definida punto a punto")
