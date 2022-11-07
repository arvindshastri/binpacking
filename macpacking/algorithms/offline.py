from .. import Solution, WeightSet
from ..model import Offline
from macpacking.algorithms.online import \
    FirstFit, BestFit, WorstFit, NextFitOnline
import binpacking as bp


class BenMaier(Offline):

    def _process(self, capacity: int, weights: list[int]) -> Solution:
        self.comparisons = 0
        return bp.to_constant_volume(weights, capacity)


class FixedNumBins(Offline):

    def __init__(self, numBins):
        self.numBins = numBins
        self.comparisons = 0

    def _process(self, capacity: int, weights: list[int]) -> Solution:
        return bp.to_constant_bin_number(weights, self.numBins)


class MultiFit(Offline):

    def __init__(self, numBins):
        self.numBins = numBins
        self.comparisons = 0

    def _process(self, capacity: int, weights: list[int]) -> Solution:
        
        L = max((sum(weights) / self.numBins), max(weights))    # lower bound
        U = max(2*(sum(weights) / self.numBins), max(weights))  # upper bound
        k = 10  #iterations

        for _ in range(k):
            C = (L+U)/2  # set capacity
            delegation = FirstFitDecreasing()
            FFDoutput = delegation((C, weights))  # delegate to FFD
            self.comparisons += delegation.comparisons  # increase comparisons 

            if len(FFDoutput) <= self.numBins:
                U = C  # if FFD needs at most numBins
            else:
                L = C  # if FFD needs more than numBins
        
        delegation = FirstFitDecreasing() 
        output = delegation((U, weights))  # output guaranteed to use at most numBins
        self.comparisons += delegation.comparisons
        return output


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
