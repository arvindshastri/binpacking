from .. import Solution, WeightStream
from ..model import Online


class WorstFit(Online):

    def _process(self, capacity: int, stream: WeightStream) -> Solution:

        solution = []

        for w in stream:
            max = -1
            worst_index = 0

            for i in range(len(solution)):
                remaining = capacity - sum(solution[i])
                if (remaining >= w and remaining > max):
                    worst_index = i
                    max = remaining

            if (max == -1):
                solution.append([w])
            else:
                solution[worst_index].append(w)

        return solution
