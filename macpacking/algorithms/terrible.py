from .. import Solution, WeightStream
from ..model import Online


class Terrible(Online):

    def _process(self, capacity: int, stream: WeightStream) -> Solution:
        bin_index = 0
        solution = []
        for w in stream:
            bin_index += 1
            solution.append([w])
        return solution