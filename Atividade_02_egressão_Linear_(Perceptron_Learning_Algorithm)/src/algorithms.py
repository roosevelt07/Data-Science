import numpy as np
import abc
import src.optimizers as opt
import src.models as models 
import src.stop_criteria as stop
from src.preprocessing import Preprocessing

class Algorithm(abc.ABC):
    def __init__(self, optimizer_strategy: opt.OptimizerStrategy, model: models.Model) -> None:
        self.algorithm_observers = []
        self.optimizer_strategy = optimizer_strategy
        self.model = model
       
    def add(self, observer):
       if observer not in self.algorithm_observers:
           self.algorithm_observers.append(observer)
       else:
           print('Failed to add: {}'.format(observer))
 
    def remove(self, observer):
       try:
           self.algorithm_observers.remove(observer)
       except ValueError:
           print('Failed to remove: {}'.format(observer))
 
    def notify_iteration(self):
        [o.notify_iteration(self) for o in self.algorithm_observers]
 
    def notify_started(self):
        [o.notify_started(self) for o in self.algorithm_observers]
 
    def notify_finished(self):
        [o.notify_finished(self) for o in self.algorithm_observers]
 
    @abc.abstractmethod
    def fit(self):
        """Implement the fit method"""
 
    @property
    def iteration(self):
        return self._iteration
 
    @iteration.setter
    def iteration(self, value):
        self._iteration = value    
 
    @property
    def errors(self):
        return self._errors
   
    @errors.setter
    def errors(self, value):
        self._errors = value
 
    @property
    def rmse(self):
        return self._rmse
   
    @rmse.setter
    def rmse(self, value):
        self._rmse = value
 
    
    @property
    def error(self):
        return self.rmse
   
 
class PLA(Algorithm):
 
    def fit(self, X: np.array, y: np.array, stop_criteria: stop.StopCriteria):
        self.iteration = 0
        self.__initialize(X)
        while True:
            self.__update_error(y)
            self.notify_iteration()
            self.optimizer_strategy.update_model(self.Xd, y, self.model)
            self.iteration = self.iteration + 1
            if stop_criteria.isFinished(self):
                self.notify_finished()
                break
 
    def __update_error(self, y):
        self.yhat = self.model.predict(self.Xd)
        self.errors = self.yhat - y
        self.rmse = 1.0/len(self.Xd) * np.square(np.linalg.norm(self.errors))
        
    def __initialize(self, X):
        self.Xd = Preprocessing.build_design_matrix(X)
        self.model.w = Preprocessing.initialize_weights(self.Xd)
        self.notify_started()