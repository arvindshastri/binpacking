from .. import Solution, WeightStream
from ..model import Online


class BestFit(Online):

    def _process(self, capacity: int, stream: WeightStream) -> Solution:

        solution = []
        self.comparisons = 0

        for w in stream:
            min = capacity + 1
            best_bin = 0

            for i in range(len(solution)):
                self.comparisons += 1
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
        self.comparisons = 0

        for w in stream:
            bin_index = 0

            while (bin_index < len(solution)):
                self.comparisons += 1
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
        self.comparisons = 0

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
        self.comparisons = 0

        for w in stream:
            solution.append([w])
            bin_index += 1

        return solution


class WorstFit(Online):

    def _process(self, capacity: int, stream: WeightStream) -> Solution:

        solution = []
        self.comparisons = 0

        for w in stream:
            max = -1
            worst_index = 0

            for i in range(len(solution)):
                self.comparisons += 1
                remaining = capacity - sum(solution[i])
                if (remaining >= w and remaining > max):
                    worst_index = i
                    max = remaining

            if (max == -1):
                solution.append([w])
            else:
                solution[worst_index].append(w)

        return solution


class RefinedFirstFit(Online):

    def _process(self, capacity: int, stream: WeightStream) -> Solution:

        self.comparisons = 0
        fixedIntegers = [6, 7, 8, 9]
        class1_bins = []
        class2_bins = []
        class3_bins = []
        class4_bins = []
        solution = []
        seen = 0

        for w in stream:

            selectedBin = []
            bin_index = 0
            size = w/capacity
            seen += 1

            #  A piece
            if size > (1/2):
                selectedBin = class1_bins
            #  B1 piece
            elif size > (2/5) and size <= (1/2):
                selectedBin = class2_bins
            #  B2 piece
            elif size > (1/3) and size <= (2/5):
                if any(seen % m == 0 for m in fixedIntegers):
                    selectedBin = class1_bins
                else:
                    selectedBin = class3_bins
            #  X piece
            else:
                selectedBin = class4_bins

            while (bin_index < len(selectedBin)):
                self.comparisons += 1
                if (capacity - sum(selectedBin[bin_index]) >= w):
                    selectedBin[bin_index].append(w)
                    break
                bin_index += 1

            if bin_index == len(selectedBin):
                selectedBin.append([w])

        solution = class1_bins + class2_bins + class3_bins + class4_bins

        return solution
