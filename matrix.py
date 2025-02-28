"""#8"""

from typing import List

import doctest


def matrix_multiply(matrix1: List[List[int]], matrix2: List[List[int]]) -> List[List[int]]:
    """
    Множить дві матриці.

    Arguments:
        matrix1 (List[List[int]]): Перша матриця.
        matrix2 (List[List[int]]): Друга матриця.
    
    Returns:
        List[List[int]]: Перемножені матриці.
    
    Raises:
        ValueError: Якщо одна з матриць порожня, якщо кількість стовпців першої матриці не дорівнює 
            кількості рядків другої матриці, або якщо рядки матриць мають різну довжину чи порожні.
        TypeError: Якщо одна з матриць не є списком списків або якщо елементи матриць не є int.

    >>> matrix_multiply([[1, 2], [3, 4]], [[5, 6], [7, 8]])
    [[19, 22], [43, 50]]
    >>> matrix_multiply([[1, 2], [3, 4]], [])
    Traceback (most recent call last):
        ...
    ValueError: Матриці не можуть бути порожніми
    >>> matrix_multiply(([1, 2], [3, 4]), [[5, 6], [7, 8]])
    Traceback (most recent call last):
        ...
    TypeError: 'matrix1' повинна бути списком('list') зі списками('list') всередині
    >>> matrix_multiply([[1, 2], [3, 4]], [(5, 6), (7, 8)])
    Traceback (most recent call last):
        ...
    TypeError: 'matrix2' повинна бути списком('list') зі списками('list') всередині
    >>> matrix_multiply([[1, 2], [3]], [[5, 6], [7, 8]])
    Traceback (most recent call last):
        ...
    ValueError: Усі рядки в матрицях мають бути однакової довжини і не порожні
    >>> matrix_multiply([[1, 2], []], [[5, 6], [7, 8]])
    Traceback (most recent call last):
        ...
    ValueError: Усі рядки в матрицях мають бути однакової довжини і не порожні
    >>> matrix_multiply([[1, 2], [3, 'a']], [[5, 6], [7, 8]])
    Traceback (most recent call last):
        ...
    TypeError: Усі елементи матриць мають бути цілими числами
    """
    if not matrix1 or not matrix2:
        raise ValueError("Матриці не можуть бути порожніми")

    if not isinstance(matrix1, list) or not all(isinstance(row, list) for row in matrix1):
        raise TypeError("'matrix1' повинна бути списком('list') зі списками('list') всередині")

    if not isinstance(matrix2, list) or not all(isinstance(row, list) for row in matrix2):
        raise TypeError("'matrix2' повинна бути списком('list') зі списками('list') всередині")

    # Перевірка, чи всі рядки мають однакову довжину і не порожні
    row_lengths = {len(row) for row in matrix1 + matrix2}
    if len(row_lengths) > 1 or 0 in row_lengths:
        raise ValueError("Усі рядки в матрицях мають бути однакової довжини і не порожні")

    # Перевірка, чи всі елементи є цілими числами
    for row in matrix1 + matrix2:
        if not all(isinstance(x, int) for x in row):
            raise TypeError("Усі елементи матриць мають бути цілими числами")

    rows_matrix1, cols_matrix1 = len(matrix1), len(matrix1[0])
    rows_matrix2, cols_matrix2 = len(matrix2), len(matrix2[0])

    if cols_matrix1 != rows_matrix2:
        raise ValueError("Кількість стовпців першої матриці має дорівнювати кількості рядків другої матриці")

    result = [[0] * cols_matrix2 for _ in range(rows_matrix1)]

    for i in range(rows_matrix1):
        for j in range(cols_matrix2):
            for k in range(cols_matrix1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result


def transpose_matrix(matrix):
    """
    Транспонує матрицю, обмінюючи її рядки та стовпці.

    Arguments:
        matrix (List[List[Any]]): Вхідна матриця.
    
    Returns:
        List[List[Any]]: Транспонована матриця.

    Raises:
        TypeError: Якщо вхідні дані не є списком списків.
        ValueError: Якщо рядки матриці мають різну довжину.

    >>> transpose_matrix([[1, 2], [3, 4]])
    [[1, 3], [2, 4]]
    >>> transpose_matrix([[1, 2, 3], [4, 5, 6]])
    [[1, 4], [2, 5], [3, 6]]
    >>> transpose_matrix([[1]])
    [[1]]
    >>> transpose_matrix([])
    []
    >>> transpose_matrix([[1, 2, 3]])
    [[1], [2], [3]]
    >>> transpose_matrix([[1], [2], [3]])
    [[1, 2, 3]]
    >>> transpose_matrix([1, 2, 3])
    Traceback (most recent call last):
        ...
    TypeError: Матриця повинна бути списком списків
    >>> transpose_matrix([[1, 2], [3]])
    Traceback (most recent call last):
        ...
    ValueError: Усі рядки матриці повинні мати однакову довжину
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("Матриця повинна бути списком списків")

    if len(set(len(row) for row in matrix)) > 1:
        raise ValueError("Усі рядки матриці повинні мати однакову довжину")

    return list(map(list, zip(*matrix)))


if __name__ == "__main__":
    doctest.testmod(verbose=True)
