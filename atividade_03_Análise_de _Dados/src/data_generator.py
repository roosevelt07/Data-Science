import numpy as np


class DataGenerator:

    def __init__(self, loc: float, scale: float, sample_size: int):
        self.loc = loc
        self.scale = scale
        self.sample_size = sample_size
        self.X = np.random.normal(
            loc=self.loc, scale=self.scale, size=(self.sample_size, 1))
        
    def get_data(self):
        return self.X
