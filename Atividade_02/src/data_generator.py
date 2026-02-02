import numpy as np
import scipy.stats as st
from typing import Tuple

class DataGenerator():

 def __init__(self, sample_size, weights, x_min, x_max, std=1) -> None:
        self.sample_size = sample_size
        self.weights = weights
        self.x_min = x_min
        self.x_max = x_max
        self.std = std

 def get_data(self):

       
        x0 = np.ones((self.sample_size, 1))

        
        x1 = np.array(
            [np.linspace(self.x_min, self.x_max, self.sample_size)]).T

        
        X = np.column_stack([x0, x1])

       
        y_expected = X.dot(self.weights)

       
        noise = st.norm.rvs(loc=0, scale=self.std, size=self.sample_size)
        noise.shape = (self.sample_size, 1)
        y_observed = y_expected + noise

        return x1, y_observed 