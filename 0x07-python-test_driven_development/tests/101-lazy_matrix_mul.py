The ``lazy_matrix_mul`` function
===================================

Import the function:

    >>> lazy_matrix_mul = __import__('100-matrix_mul').lazy_matrix_mul

Multiply two square matrices:

    >>> lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
    array([[ 7, 10],
           [15, 22]])

Multiply a 2x3 matrix by a 3x2 matrix:

    >>> lazy_matrix_mul([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]])
    array([[ 58,  64],
           [139, 154]])

Multiply single-element matrices:

    >>> lazy_matrix_mul([[2]], [[3]])
    array([[6]])

Multiply by an identity matrix:

    >>> lazy_matrix_mul([[1, 2], [3, 4]], [[1, 0], [0, 1]])
    array([[1, 2],
           [3, 4]])

Matrices can contain floats:

    >>> lazy_matrix_mul([[1.5, 2.5]], [[1], [2]])
    array([[6.5]])

Matrices can contain negative numbers:

    >>> lazy_matrix_mul([[-1, 2], [3, -4]], [[1, 0], [0, 1]])
    array([[-1,  2],
           [ 3, -4]])

Matrices with incompatible dimensions raise an error:

    >>> try:
    ...     lazy_matrix_mul([[1, 2, 3]], [[1, 2, 3]])
    ... except (TypeError, ValueError):
    ...     print("Error raised")
    Error raised

m_a containing a non-number raises an error:

    >>> try:
    ...     lazy_matrix_mul([[1, "a"], [3, 4]], [[1, 2], [3, 4]])
    ... except (TypeError, ValueError):
    ...     print("Error raised")
    Error raised

m_b containing a non-number raises an error:

    >>> try:
    ...     lazy_matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, "b"]])
    ... except (TypeError, ValueError):
    ...     print("Error raised")
    Error raised

m_a not a list of lists raises an error:

    >>> try:
    ...     lazy_matrix_mul(1, [[1, 2], [3, 4]])
    ... except (TypeError, ValueError):
    ...     print("Error raised")
    Error raised

m_a with rows of different sizes raises an error:

    >>> try:
    ...     lazy_matrix_mul([[1, 2], [3]], [[1, 2], [3, 4]])
    ... except (TypeError, ValueError):
    ...     print("Error raised")
    Error raised

An empty matrix raises an error:

    >>> try:
    ...     lazy_matrix_mul([], [[1, 2], [3, 4]])
    ... except (TypeError, ValueError):
    ...     print("Error raised")
    Error raised
