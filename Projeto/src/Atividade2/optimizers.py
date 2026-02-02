from tokenize import Double
import numpy as np

import abc
import src.Atividade2.models

class OptimizerStrategy(abc.ABC):
    def __init__(self, learning_rate: float) -> None:
        self.learning_rate = learning_rate
   
    
    @abc.abstractmethod
    def update_model(self, X, y, model):
        return model.update_model(X, y)
        """Implement Update Weigth Strategy"""
    
class SteepestDescentMethod(OptimizerStrategy):

    def update_model(self, X, y, model):           
        model.w = model.w - self.learning_rate*(2.0/len(X)) * (np.linalg.multi_dot([X.T, X, model.w]) - np.dot(X.T,y))

class NewtonsMethod(OptimizerStrategy):

    def update_model(self, X, y, model):
        model.w = (1 - self.learning_rate)* model.w + self.learning_rate *  np.linalg.multi_dot([np.linalg.inv(np.dot(X.T, X)), X.T, y])
    