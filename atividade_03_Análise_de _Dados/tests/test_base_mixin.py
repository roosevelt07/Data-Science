import unittest
from abc import ABC, abstractmethod
import numpy as np
from src.data_generator import DataGenerator

class TestBaseMixin(unittest.TestCase, ABC):

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)

    def setUp(self) -> None:
        np.random.seed(0)
        super().setUp()
        self._sample_size = 1000
        self._loc = 10
        self._scale = 2
        self.generate_data()
        
        
    def generate_data(self):
        self.data = DataGenerator(self.loc, self.scale, self.sample_size)
        X = self.data.get_data()
        self._X = X

        
    @property
    def sample_size(self):
        return self._sample_size

    @property
    def loc(self):
        return self._loc

    @property
    def scale(self):
        return self._scale
    
    @property
    def X(self):
        return self._X