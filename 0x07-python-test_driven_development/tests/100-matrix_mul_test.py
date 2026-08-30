#!/usr/bin/python3
"""Unittest for matrix_mul(m_a, m_b)
"""
import unittest
matrix_mul = __import__('100-matrix_mul').matrix_mul


class TestMatrixMul(unittest.TestCase):
    """Tests for the matrix_mul function."""

    def test_square_matrices(self):
        m_a = [[1, 2], [3, 4]]
        m_b = [[1, 2], [3, 4]]
        self.assertEqual(matrix_mul(m_a, m_b), [[7, 10], [15, 22]])

    def test_rectangular_matrices(self):
        m_a = [[1, 2, 3], [4, 5, 6]]
        m_b = [[7, 8], [9, 10], [11, 12]]
        self.assertEqual(matrix_mul(m_a, m_b), [[58, 64], [139, 154]])

    def test_single_element_matrices(self):
        self.assertEqual(matrix_mul([[2]], [[3]]), [[6]])

    def test_identity_matrix(self):
        m_a = [[1, 2], [3, 4]]
        identity = [[1, 0], [0, 1]]
        self.assertEqual(matrix_mul(m_a, identity), [[1, 2], [3, 4]])

    def test_matrices_with_floats(self):
        m_a = [[1.5, 2.5]]
        m_b = [[1], [2]]
        self.assertEqual(matrix_mul(m_a, m_b), [[6.5]])

    def test_matrices_with_negatives(self):
        m_a = [[-1, 2], [3, -4]]
        m_b = [[1, 0], [0, 1]]
        self.assertEqual(matrix_mul(m_a, m_b), [[-1, 2], [3, -4]])

    def test_result_is_not_original_matrix(self):
        m_a = [[1, 2], [3, 4]]
        m_b = [[1, 0], [0, 1]]
        result = matrix_mul(m_a, m_b)
        self.assertIsNot(result, m_a)

    def test_m_a_not_a_list(self):
        with self.assertRaises(TypeError) as context:
            matrix_mul(1, [[1, 2], [3, 4]])
        self.assertEqual(str(context.exception), "m_a must be a list")

    def test_m_b_not_a_list(self):
        with self.assertRaises(TypeError) as context:
            matrix_mul([[1, 2], [3, 4]], "School")
        self.assertEqual(str(context.exception), "m_b must be a list")

    def test_m_a_not_a_list_of_lists(self):
        with self.assertRaises(TypeError) as context:
            matrix_mul([1, 2], [[1, 2], [3, 4]])
        self.assertEqual(str(context.exception), "m_a must be a list of lists")

    def test_m_b_not_a_list_of_lists(self):
        with self.assertRaises(TypeError) as context:
            matrix_mul([[1, 2], [3, 4]], [1, 2])
        self.assertEqual(str(context.exception), "m_b must be a list of lists")

    def test_m_a_empty_list(self):
        with self.assertRaises(ValueError) as context:
            matrix_mul([], [[1, 2], [3, 4]])
        self.assertEqual(str(context.exception), "m_a can't be empty")

    def test_m_a_empty_list_of_list(self):
        with self.assertRaises(ValueError) as context:
            matrix_mul([[]], [[1, 2], [3, 4]])
        self.assertEqual(str(context.exception), "m_a can't be empty")

    def test_m_b_empty_list(self):
        with self.assertRaises(ValueError) as context:
            matrix_mul([[1, 2], [3, 4]], [])
        self.assertEqual(str(context.exception), "m_b can't be empty")

    def test_m_a_contains_non_number(self):
        with self.assertRaises(TypeError) as context:
            matrix_mul([[1, "a"], [3, 4]], [[1, 2], [3, 4]])
        self.assertEqual(
            str(context.exception),
            "m_a should contain only integers or floats")

    def test_m_b_contains_non_number(self):
        with self.assertRaises(TypeError) as context:
            matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, "b"]])
        self.assertEqual(
            str(context.exception),
            "m_b should contain only integers or floats")

    def test_m_a_rows_different_size(self):
        with self.assertRaises(TypeError) as context:
            matrix_mul([[1, 2], [3]], [[1, 2], [3, 4]])
        self.assertEqual(
            str(context.exception),
            "each row of m_a must be of the same size")

    def test_m_b_rows_different_size(self):
        with self.assertRaises(TypeError) as context:
            matrix_mul([[1, 2], [3, 4]], [[1, 2], [3]])
        self.assertEqual(
            str(context.exception),
            "each row of m_b must be of the same size")

    def test_incompatible_dimensions(self):
        with self.assertRaises(ValueError) as context:
            matrix_mul([[1, 2, 3]], [[1, 2, 3]])
        self.assertEqual(
            str(context.exception), "m_a and m_b can't be multiplied")


if __name__ == '__main__':
    unittest.main()
