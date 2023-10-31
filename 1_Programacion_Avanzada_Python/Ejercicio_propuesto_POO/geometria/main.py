from geom2d.vector import Vector
from geom2d.punto import Punto


def main():
    # Crear instancias de Vector
    vector1 = Vector(3, 4)
    vector2 = Vector(1, 2)
    # Operaciones con Vector
    result_vector = vector1 + vector2
    print("Vector Sum:", result_vector)

    result_vector = vector1 - vector2
    print("Vector Subtraction:", result_vector)

    punto1 = Punto(1, 2)
    print(punto1)
    punto2 = Punto(3, 3)
    print(punto2)
    # Prueba del metodo sub con los puntos:
    resta = punto2 - punto1  # Funcionamiento correcto V(2,1)
    print(resta)
    dist_ptos = punto1.distance(punto2)  # Correcto = 2.236
    print(dist_ptos)
    print("")


if __name__ == '__main__':
    main()
