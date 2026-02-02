import numpy as np

class MatrixSolver:
    @staticmethod
    def solve_invertible(X: np.ndarray, y: np.ndarray) -> np.ndarray:
        return np.linalg.inv(X) @ y

    @staticmethod
    def solve_non_invertible(X: np.ndarray, y: np.ndarray) -> np.ndarray:
        return np.linalg.pinv(X) @ y