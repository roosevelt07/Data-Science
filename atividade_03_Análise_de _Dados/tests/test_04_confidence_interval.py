import unittest
import numpy as np
import scipy.stats as st
from src.bootstrap import Bootstrap
from src.confidence_interval import ConfidenceInterval
from tests.test_base_mixin import TestBaseMixin

class TestConfidenceInterval(TestBaseMixin):
    
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.alpha = 0.05
    def setUp(self) -> None:
        super().setUp()
        self.confidence_interval = ConfidenceInterval(data=self.X[:,0], alpha=0.05)

    def test_01_lower_bound(self):
        expected = 9.78
        actual = self.confidence_interval.calculate_lower_bound()
        self.assertAlmostEqual(expected, actual, delta=0.01)

    def test_02_upper_bound(self):
        expected = 10.03
        actual = self.confidence_interval.calculate_upper_bound()
        self.assertAlmostEqual(expected, actual,delta=0.01)

if __name__ == '__main__':
    unittest.main()