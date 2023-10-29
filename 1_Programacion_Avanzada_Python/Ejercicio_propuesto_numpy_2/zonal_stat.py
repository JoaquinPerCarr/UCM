import numpy as np
import doctest


def read_data(fname: str, tipo: type) -> np.ndarray:
    """
    Reading places or values.
    Args:
        fname: Str with name of file
        tipo: type(int or float) of data content in file "fname"

    Returns: Loaded data in a numpy array

    Examples
    --------
    >>> read_data("./datos/zonas.txt",np.int_)
    array([[1, 1, 1, 1, 3, 3],
           [1, 1, 1, 1, 3, 1],
           [2, 2, 3, 3, 3, 4],
           [2, 2, 3, 3, 3, 4],
           [2, 2, 3, 3, 2, 2],
           [3, 3, 3, 3, 3, 2]])
   >>> read_data("./datos/valores.txt",np.float_)
   array([[5., 3., 4., 4., 4., 2.],
          [2., 1., 4., 2., 6., 3.],
          [8., 4., 3., 5., 3., 1.],
          [4., 2., 4., 3., 2., 2.],
          [6., 3., 3., 7., 4., 2.],
          [5., 5., 2., 3., 1., 3.]])
    """
    try:
        datos = np.loadtxt(fname, dtype=tipo)
        return datos
    except FileNotFoundError:
        raise FileNotFoundError(f'Input file {fname} not found')


def set_of_areas(zonas: np.ndarray) -> set[int]:
    """
    Distinguish different areas in an array
    Args:
        zonas: Array with differents areas.

    Returns: The number of areas with are different.

    Examples:
    --------
    >>> set_of_areas(np.arange(10).reshape(5, 2))
    {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    >>> set_of_areas(np.zeros(10, dtype=np.int_).reshape(5, 2))
    {0}
    >>> set_of_areas(np.array([2, 3, 4, 2, 3, 4], dtype=np.int_).reshape(3, 2))
    {2, 3, 4}
    >>> set_of_areas(np.zeros(3, dtype=np.float_))
    Traceback (most recent call last):
        ...
    TypeError: The elements type must be int, not float64
    """
    if zonas.dtype == int:
        area = zonas.flatten()
        return set(area)
    else:
        raise TypeError("The elements type must be int, not {}".format(zonas.dtype))


def mean_areas(zonas: np.ndarray, valores: np.ndarray) -> np.ndarray:
    """
    Calculate means from zones and values txt files.
    Args:
        zonas: Array with zones
        valores: Array with the values of the different zones

    Returns: Array with means of the values of zones.

    Examples
    --------
    >>> mean_areas(np.array([[1, 1, 3], [2, 2, 3]]), np.array([[10, 1, 1], [1, 1, 1]])) # Dimensions are equal
    array([[5.5, 5.5, 1. ],
           [1. , 1. , 1. ]])

    >>> mean_areas(np.array([[1, 1, 3], [2, 2, 3]]), np.array([[10, 1], [1, 1]]))       # Shapes aren't equal
    Traceback (most recent call last):
    ...
    IndexError: Shape of zonas and valores must be the same. zonas: (2, 3) != valores: (2, 2)

    >>> mean_areas(np.array([[1.4, 1.2, 3], [2, 2, 3]]), np.array([[10, 1], [1, 1]]))   # Zones array with float data type
    Traceback (most recent call last):
    ...
    TypeError: The elements type must be int, not float64

    >>> mean_areas(np.array([[1, 1, 3], [2, 0, 0]]), np.array([[10, 1, 1], [1, 1, 1]])) # Array with zero zones (Zero represents no zone to do the mean value later)
    array([[5.5, 5.5, 1. ],
           [1. , 0. , 0. ]])
    """
    if zonas.dtype != np.int_:
        raise TypeError("The elements type must be int, not {}".format(zonas.dtype))
    elif zonas.shape != valores.shape:
        raise IndexError(f'Shape of zonas and valores must be the same. zonas: {zonas.shape} != valores: {valores.shape}')
    else:
        num_zonas = set(zonas.flatten())
        array_resultado = np.zeros((zonas.shape[0], zonas.shape[1]))

        for zona in num_zonas:
            if zona != 0:  # Zero-zone represents empty zone in this array.
                mascara = zonas == zona
                array_resultado[mascara] = valores[mascara].mean().round(1)   # By making the mask, we know the positions of the zones that are at True.
                                                                              # We average all of these and save them in the empty array positions with
                                                                              # that value. Round(1) indicates that the float is displayed with a decimal.
        return array_resultado


# ------------ Test  ------------#
def test_doc() -> None:
    """
    The following instructions are to execute the tests of same functions
    If any test is fail, we will receive the notice when executing
    :return: None
    """
    doctest.run_docstring_examples(read_data, globals(), verbose=True)  # vemos los resultados de los test que fallan
    doctest.run_docstring_examples(set_of_areas, globals(), verbose=True)  # vemos los resultados de los test que fallan
    doctest.run_docstring_examples(mean_areas, globals(), verbose=True)  # vemos los resultados de los test que fallan


if __name__ == "__main__":
    test_doc()   # executing tests
