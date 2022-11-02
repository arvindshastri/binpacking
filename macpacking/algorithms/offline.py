from .. import Solution, WeightSet
from ..model import Offline
from macpacking.algorithms.online import \
    FirstFit, BestFit, WorstFit, NextFitOnline
import binpacking as bp


class BenMaier(Offline):

    def _process(self, capacity: int, weights: list[int]) -> Solution:
        return bp.to_constant_volume(weights, capacity)


class BestFitDecreasing(Offline):

    def _process(self, capacity: int, weights: WeightSet) -> Solution:
        weights = sorted(weights, reverse=True)
        delegation = BestFit()
        output = delegation((capacity, weights))
        self.comparisons = delegation.comparisons
        return output


class FirstFitDecreasing(Offline):

    def _process(self, capacity: int, weights: WeightSet) -> Solution:
        weights = sorted(weights, reverse=True)
        delegation = FirstFit()
        output = delegation((capacity, weights))
        self.comparisons = delegation.comparisons
        return output


class NextFitOffline(Offline):

    def _process(self, capacity: int, weights: WeightSet) -> Solution:
        weights = sorted(weights, reverse=True)
        delegation = NextFitOnline()
        output = delegation((capacity, weights))
        self.comparisons = delegation.comparisons
        return output


class WorstFitDecreasing(Offline):

    def _process(self, capacity: int, weights: WeightSet) -> Solution:
        weights = sorted(weights, reverse=True)
        delegation = WorstFit()
        output = delegation((capacity, weights))
        self.comparisons = delegation.comparisons
        return output
