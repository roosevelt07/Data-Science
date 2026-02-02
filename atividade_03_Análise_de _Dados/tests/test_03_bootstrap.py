
import unittest
import numpy as np
from tests.test_base_mixin import TestBaseMixin
from src.bootstrap import Bootstrap

class TestBootstrap(TestBaseMixin):

    
    def setUp(self) -> None:
        super().setUp()
        self.bootstrap = Bootstrap(self.X[:,0])
        self.bootstrap.calculate_bootstrap(bootstraps=9999, estimator=np.mean)
    
    def test_01_mean(self):
        expected = self.loc
        actual = self.bootstrap.mean()
        self.assertAlmostEqual(expected, actual, delta=0.1)

    def test_02_std(self):
        expected = 0
        actual = self.bootstrap.std()
        self.assertAlmostEqual(expected, actual, delta=0.5)
    

if __name__ == '__main__':
    unittest.main()