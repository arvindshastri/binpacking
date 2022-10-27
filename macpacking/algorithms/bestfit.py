from .. import Solution, WeightStream
from ..model import Online


class BestFit(Online):

    def _process(self, capacity: int, stream: WeightStream) -> Solution:

        solution = []

        for w in stream:
            min = capacity + 1
            best_bin = 0

            for i in range(len(solution)):
                remaining = capacity - sum(solution[i])
                if (remaining >= w) and (remaining < min):
                    best_bin = i
                    min = remaining

            if (min == capacity + 1):
                solution.append([w])
            else:
                solution[best_bin].append(w)

        return solution
