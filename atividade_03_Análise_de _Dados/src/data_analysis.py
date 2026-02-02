import numpy as np


class DataAnalysis:

    def __init__(self, X) -> None:
        self.X = X

    def cdf_value(self, x) -> float:    
        return np.mean(self.X <= x)