from .. import Solution, WeightSet
from ..model import Offline
from .worstfit import WorstFit as worstfit


class WorstFitDecreasing(Offline):

    def _process(self, capacity: int, weights: WeightSet) -> Solution:
        weights = sorted(weights, reverse=True)
        delegation = worstfit()
        return delegation((capacity, weights))
