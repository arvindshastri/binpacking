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


class FirstFit(Online):

    def _process(self, capacity: int, stream: WeightStream) -> Solution:

        solution = []

        for w in stream:
            bin_index = 0

            while (bin_index < len(solution)):
                if (capacity - sum(solution[bin_index]) >= w):
                    solution[bin_index].append(w)
                    break
                bin_index += 1

            if bin_index == len(solution):
                solution.append([w])

        return solution


class NextFitOnline(Online):

    def _process(self, capacity: int, stream: WeightStream) -> Solution:
        bin_index = 0
        solution = [[]]
        remaining = capacity

        for w in stream:

            if remaining >= w:
                solution[bin_index].append(w)
                remaining = remaining - w
            else:
                bin_index += 1
                solution.append([w])
                remaining = capacity - w

        return solution


class Terrible(Online):

    def _process(self, capacity: int, stream: WeightStream) -> Solution:
        bin_index = 0
        solution = []
        for w in stream:
            solution.append([w])
            bin_index += 1
        return solution


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
