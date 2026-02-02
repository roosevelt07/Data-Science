import unittest
import numpy as np
from src.data_generator import DataGenerator
from tests.test_base_mixin import TestBaseMixin


class TestDataGenerator(TestBaseMixin):

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        
    def setUp(self) -> None:
        return super().setUp()
   
   
    def test_01_x_shape(self):
        expected = (super().sample_size, 1)
        actual = self.X.shape
        self.assertEqual(actual, expected)

    def test_02_x_mean(self):
        expected = self.loc
        actual = np.mean(self.X[:,0])
        self.assertAlmostEqual(actual, expected, delta=0.1)

    def test_03_x_std(self):
        expected = self.scale
        actual = np.std(self.X[:,0])
        self.assertAlmostEqual(actual, expected, delta=0.2)

if __name__ == '__main__':
    unittest.main()