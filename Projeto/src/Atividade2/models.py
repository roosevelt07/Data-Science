import numpy as np
import abc

class Model(abc.ABC):
    def __init__(self) -> None:
        super().__init__()

    @abc.abstractmethod
    def predict(self, X: np.ndarray) -> np.ndarray:
        pass

    @property
    def w(self):
        return self._w

    @w.setter
    def w(self, value):
        self._w = value


class LinearModel(Model):
    def __init__(self) -> None:
        super().__init__()
        self._w = None  

    def predict(self, X: np.ndarray) -> np.ndarray:
        return X @ self._w