import numpy as np
import scipy.stats as st

class Preprocessing:

    @staticmethod
    def build_design_matrix(X):
        bias = np.ones((X.shape[0], 1))
        return np.hstack((bias, X))

    @staticmethod
    def initialize_weights(X):
        w = np.random.randn(X.shape[1])  
        return np.array([w]).T