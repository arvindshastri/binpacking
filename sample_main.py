from macpacking.reader import DatasetReader, BinppReader, JburkardtReader
from macpacking.model  import Online, Offline
import macpacking.algorithms.offline as offline

filename1 = '_datasets/jburkardt/p01_c.txt'
filename2 = '_datasets/jburkardt/p01_s.txt'
filename3 = '_datasets/jburkardt/p01_w.txt'

reader: DatasetReader = JburkardtReader(filename1, filename2, filename3)
print(f'  - Bin Capacity: {reader.offline()[0]}')
print(f'  - Objects to pack: {sorted(reader.offline()[1])}')

import macpacking.algorithms.baseline as baseline
strategy: Offline = baseline.BenMaier()
result = strategy(reader.offline())
print(f'nb_bins = {len(result)}')
print(f'baseline = {sorted(result)}')

import macpacking.algorithms.firstfit as firstfit
strategy: Online = firstfit.FirstFit()
result = strategy(reader.online())
print(f'nb_bins = {len(result)}')
print(f'firstfit = {sorted(result)}')

import macpacking.algorithms.bestfit as bestfit
strategy: Online = bestfit.BestFit()
result = strategy(reader.online())
print(f'nb_bins = {len(result)}')
print(f'bestfit = {sorted(result)}')

import macpacking.algorithms.worstfit as worstfit
strategy: Online = worstfit.WorstFit()
result = strategy(reader.online())
print(f'nb_bins = {len(result)}')
print(f'worstfit = {sorted(result)}')

import macpacking.algorithms.firstfitdecreasing as firstfitdecreasing
strategy: Offline = firstfitdecreasing.FirstFitDecreasing()
result = strategy(reader.offline())
print(f'nb_bins = {len(result)}')
print(f'firstfitdecreasing = {sorted(result)}')

import macpacking.algorithms.bestfitdecreasing as bestfitdecreasing
strategy: Offline = bestfitdecreasing.BestFitDecreasing()
result = strategy(reader.offline())
print(f'nb_bins = {len(result)}')
print(f'bestfitdecreasing = {sorted(result)}')

import macpacking.algorithms.worstfitdecreasing as worstfitdecreasing
strategy: Offline = worstfitdecreasing.WorstFitDecreasing()
result = strategy(reader.offline())
print(f'nb_bins = {len(result)}')
print(f'worstfitdecreasing = {sorted(result)}')

