from .. import Solution, WeightStream
from ..model import Online


class WorstFit(Online):

    def _process(self, capacity: int, stream: WeightStream) -> Solution:
        
        solution = []

        for w in stream:
            max = -1
            worst_index = 0

            for i in range(len(solution)):
                if (capacity - sum(solution[i]) >= w and capacity - sum(solution[i]) + w > max):
                    worst_index = i
                    max = capacity - sum(solution[i]) + w
            
            if (max == -1):
                solution.append([w])
            else:
                solution[worst_index].append(w)
        
        return solution