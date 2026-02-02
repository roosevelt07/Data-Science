from __future__ import annotations
import numpy as np
import scipy.stats as st
import abc
import src.optimizers as opt



class Model(abc.ABC):

    def __init__(self) -> None:
        self._w = None
        super().__init__()

    @abc.abstractmethod
    def predict(self, X: np.array) -> np.ndarray:
        """Implement the predict method"""

    @abc.abstractmethod
    def gradient(self, X: np.array, y: np.array) -> np.ndarray:
        """Implement gradient"""

    @abc.abstractmethod
    def hessian(self, X: np.array, y: np.array) -> np.ndarray:
        """Implement hessian"""

    @abc.abstractmethod
    def error(self, X, y):
        """Implement error""" 

    @property
    def w(self):
        return self._w

    @w.setter
    def w(self, value):
        self._w = value


class LinearModel(Model):

    def __init__(self) -> None:
        pass

    def predict(self, X: np.ndarray) -> np.ndarray:
        return np.dot(X, self.w)

    def gradient(self, X: np.array, y: np.array) -> np.ndarray:
        return (2/len(X)) * (np.linalg.multi_dot([X.T, X, self.w]) - np.dot(X.T, y))

    def hessian(self, X: np.array, y: np.array) -> np.ndarray:
        return (2/len(X))*np.dot(X.T, X)

    def error(self, X, y):
        yhat = self.predict(X)
        errors = yhat - y
        rmse = 1.0/len(X) * np.square(np.linalg.norm(errors))
        return rmse


class LogisticModel(Model):
    def predict(self, X: np.array) -> np.ndarray:
      
        return 1/(1+np.exp(-np.dot(X, self.w)))

    def gradient(self, X: np.array, y: np.array) -> np.ndarray:
       
        predicted = self.predict(X)
        error = predicted - y.reshape(-1, 1)
        gradient = np.dot(X.T, error)
        return gradient

    def hessian(self, X: np.array, y: np.array) -> np.ndarray:
       
        predicted_prob = self.predict(X)
        diag = np.diagflat(predicted_prob * (1 - predicted_prob))
        hessian = np.dot(np.dot(X.T, diag), X)
        return hessian

    def error(self, X, y):
        
        p = self.predict(X)
        return - np.sum(y * np.log(p) + (1-y) * np.log(1-p))
