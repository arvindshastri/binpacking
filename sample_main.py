from macpacking.reader import DatasetReader, BinppReader, JburkardtReader
from macpacking.model  import Online, Offline
import macpacking.algorithms.offline as offline

filename1 = '_datasets/jburkardt/p01_c.txt'
filename2 = '_datasets/jburkardt/p01_s.txt'
filename3 = '_datasets/jburkardt/p01_w.txt'

reader: DatasetReader = JburkardtReader(filename1, filename2, filename3)
print(f'  - Bin Capacity: {reader.offline()[0]}')
print(f'  - Objects to pack: {sorted(reader.offline()[1])}')

# import macpacking.algorithms.baseline as baseline
# strategy: Offline = baseline.BenMaier()
# result = strategy(reader.offline())
# print(f'nb_bins = {len(result)}')
# print(f'{sorted(result)}')

import macpacking.algorithms.terrible as terrible
strategy: Online = terrible.Terrible()
result = strategy(reader.online())
print(f'nb_bins = {len(result)}')
print(f'{sorted(result)}')

