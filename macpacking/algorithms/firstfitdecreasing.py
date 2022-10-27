from .. import Solution, WeightSet
from ..model import Offline
from .firstfit import FirstFit as firstfit


class FirstFitDecreasing(Offline):

    def _process(self, capacity: int, weights: WeightSet) -> Solution:
        weights = sorted(weights, reverse=True)
        delegation = firstfit()  # delegation is an object of firstfit class
        return delegation((capacity, weights))
