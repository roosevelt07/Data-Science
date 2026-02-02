from __future__ import annotations
import numpy as np
import scipy.stats as st
import abc
import src.models as models

class OptimizerStrategy(abc.ABC):
    def __init__(self, learning_rate: float) -> None:
        self.learning_rate = learning_rate

    @abc.abstractmethod
    def update_model(self, X, y, model: models.Model):
        """Implement Update Weigth Strategy"""


class NewtonsMethod(OptimizerStrategy):

    def update_model(self, X, y, model: models.Model):
        # newton's method
        gradient = model.gradient(X, y)
        hessian = model.hessian(X, y)
        inverse_hessian = np.linalg.inv(hessian)
        model.w = model.w - self.learning_rate * \
            np.dot(inverse_hessian, gradient)


class SteepestDescentMethod(OptimizerStrategy):

    def update_model(self, X, y, model: models.Model):
        # steepest descent method
        gradient = model.gradient(X, y)
        model.w = model.w - self.learning_rate * gradient
