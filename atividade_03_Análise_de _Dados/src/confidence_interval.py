import numpy as np
from src.bootstrap import Bootstrap as bs
from scipy import stats as st


class ConfidenceInterval:

    def __init__(self, data: np.ndarray, alpha: float) -> None:
        self.data = data
        self.alpha = alpha
        self.bootstrap = bs(data)
        self.lower_bound = None
        self.upper_bound = None
        



    def calculate_lower_bound(self) -> float:
        self.bootstrap.calculate_bootstrap(1000, np.mean)
        self.lower_bound = self.bootstrap.mean() - st.norm.ppf(
            1 - self.alpha / 2) * self.bootstrap.std()

        return self.lower_bound
    





    def calculate_upper_bound(self) -> float:
        self.bootstrap.calculate_bootstrap(1000, np.mean)
        self.upper_bound = self.bootstrap.mean() + st.norm.ppf(1 - self.alpha/2) * \
            self.bootstrap.std()

        return self.upper_bound
        



