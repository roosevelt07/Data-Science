from typing import Callable
import numpy as np



class Bootstrap:

    def __init__(self, data: np.ndarray ) -> None:
        self.data = data
        self.bootstraps = None
        self.estimator = None



    def calculate_bootstrap(self, bootstraps: int, estimator: Callable) -> None:
       self.bootstraps = np.random.choice(self.data, size=(
            bootstraps, len(self.data)), replace=True)  
       self.estimator = estimator(self.bootstraps, axis=1)




    
    def mean(self) -> float:
        return np.mean(self.estimator)
    


    def std(self) -> float:
        return np.std(self.estimator)
          