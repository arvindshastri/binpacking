from macpacking.reader import DatasetReader, BinppReader, JburkardtReader  # noqa: F401, E501
from macpacking.model import Online, Offline  # noqa: F401
from macpacking.algorithms.online import *    # noqa: F401, F403
from macpacking.algorithms.offline import *   # noqa: F401, F403


filename1 = '_datasets/jburkardt/p02_c.txt'
# filename2 = '_datasets/jburkardt/p04_s.txt'
# filename3 = '_datasets/jburkardt/p04_w.txt'

filename = '_datasets/binpp/N1C1W1/N1C1W1_B.BPP.txt'

reader: DatasetReader = BinppReader(filename)
# reader: DatasetReader = JburkardtReader(filename1)
# print(f'  - Bin Capacity: {reader.offline()[0]}')
# print(f'  - Objects to pack: {sorted(reader.offline()[1])}')

# strategy: Offline = BenMaier()
# result = strategy(reader.offline())
# print(f'nb_bins = {len(result)}')
# print(f'baseline = {sorted(result)}')

# strategy: Online = FirstFit()
# result = strategy(reader.online())
# print(f'nb_bins = {len(result)}')
# print(f'firstfit = {sorted(result)}')

# strategy: Online = BestFit()
# result = strategy(reader.online())
# print(f'nb_bins = {len(result)}')
# print(f'bestfit = {sorted(result)}')

# strategy: Online = WorstFit()
# result = strategy(reader.online())
# print(f'nb_bins = {len(result)}')
# print(f'worstfit = {sorted(result)}')

# strategy: Offline = FirstFitDecreasing()
# result = strategy(reader.offline())
# print(f'nb_bins = {len(result)}')
# print(f'firstfitdecreasing = {sorted(result)}')

# strategy: Offline = BestFitDecreasing()
# result = strategy(reader.offline())
# print(f'nb_bins = {len(result)}')
# print(f'bestfitdecreasing = {sorted(result)}')

# strategy: Offline = WorstFitDecreasing()
# result = strategy(reader.offline())
# print(f'nb_bins = {len(result)}')
# print(f'worstfitdecreasing = {sorted(result)}')
