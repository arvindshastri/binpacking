from .. import Solution, WeightStream
from ..model import Online


class BestFit(Online):

    def _process(self, capacity: int, stream: WeightStream) -> Solution:
        
        solution = []

        for w in stream:
            bin_index = 0
            min = capacity + 1
            best_bin = 0

            for i in range(len(solution)):
                if (capacity - sum(solution[i]) >= w) and ((capacity - sum(solution[i]) + w) < min):
                    best_index = i
                    min = capacity - sum(solution[i]) + w 
            
            if (min == capacity + 1):
                solution.append([w])
            else:
                solution[best_index].append(w) 
    
        return solution
