from __future__ import annotations
from typing import List
import src.algorithms as al

import abc

class StopCriteria(abc.ABC):
    @abc.abstractmethod
    def isFinished(self, alg) -> bool:
        pass


class CompositeStopCriteria(StopCriteria):
    def __init__(self):
        self.criteria = []

    def add(self, criterion: StopCriteria):
        self.criteria.append(criterion)

    def isFinished(self, alg) -> bool:
        return any(c.isFinished(alg) for c in self.criteria)


class MinErrorStopCriteria(StopCriteria):
    def __init__(self, min_error):
        self.min_error = min_error

    def isFinished(self, algorithm):
        return algorithm.rmse <= self.min_error


class MaxIterationStopCriteria(StopCriteria):
    def __init__(self, max_iteration: int):
        self.max_iteration = max_iteration

    def isFinished(self, alg) -> bool:
        return alg.iteration >= self.max_iteration
