import numpy as np
from src.T01LinearAlgebra.P01InverseAndPseudoInverse.matrix.solvers import MatrixSolver

class TestSolve():

    def test_apartment_cost_squared(self):
        X = np.array([
            [4, 4, 120],
            [6, 2, 180],
            [2, 4, 80]
        ])
        y = np.array([
            [110000],
            [135000],
            [75000]
        ])
        expected = np.array([[12500], [7500], [250]])
        actual = MatrixSolver.solve_invertible(X, y)
        np.testing.assert_allclose(actual, expected)

    def test_apartment_cost_not_squared(self):
        X = np.array([
            [1, 1, 50, 0],
            [2, 1, 50, 0],
            [2, 1, 100, 0],
            [1, 1, 50, 1],
            [2, 1, 50, 1],
            [2, 1, 100, 1],
        ])
        y = np.array([
            [75500],
            [125500],
            [126000],
            [175500],
            [225500],
            [226000]
        ])
        expected = np.array([[50000, 25000, 10, 100000]]).T
        actual = MatrixSolver.solve_non_invertible(X, y)
        np.testing.assert_allclose(actual, expected, rtol=0.001)
