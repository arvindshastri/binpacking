from .. import Solution, WeightSet
from ..model import Offline
from .firstfit import FirstFit as firstfit


class FirstFitDecreasing(Offline):

    def _process(self, capacity: int, weights: WeightSet) -> Solution:
        weights = sorted(weights, reverse=True)
        delegation = firstfit()
        return delegation((capacity, weights))