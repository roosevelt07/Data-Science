import unittest
import numpy as np
from src.data_generator import DataGenerator
from tests.test_base_mixin import TestBaseMixin
from src.data_analysis import DataAnalysis
import scipy.stats as st

class TestDataAnalysis(TestBaseMixin):

    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        
    def setUp(self) -> None:
        super().setUp()
        self.data_analysis = DataAnalysis(self.X[:,0])
        
    
    def test_01_cdf_value_at_loc(self):
        expected = .5
        x = self.loc
        actual = self.data_analysis.cdf_value(x)
        self.assertAlmostEqual(actual, expected, delta=0.05)

    def test_02_cdf_value_at_left_extreme(self):
        
        alpha = 0.05
        expected = alpha/2
        x = self.loc - st.norm.ppf(1 - alpha/2) * self.scale
        actual = self.data_analysis.cdf_value(x)
        self.assertAlmostEqual(actual, expected, delta=0.01)

    def test_03_cdf_value_at_right_extreme(self):
        alpha = 0.05
        expected = 1 - alpha/2
        x = self.loc + st.norm.ppf(expected) * self.scale
        actual = self.data_analysis.cdf_value(x)
        self.assertAlmostEqual(actual, expected, delta=0.01)


if __name__ == '__main__':
    unittest.main()