from .. import Solution, WeightStream
from ..model import Online


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
