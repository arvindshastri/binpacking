from .. import Solution, WeightSet
from ..model import Offline
from .bestfit import BestFit as bestfit


class BestFitDecreasing(Offline):

    def _process(self, capacity: int, weights: WeightSet) -> Solution:
        weights = sorted(weights, reverse=True)
        delegation = bestfit()
        return delegation((capacity, weights))
