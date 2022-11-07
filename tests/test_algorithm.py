from macpacking.reader import DatasetReader, BinppReader
from macpacking.model  import Online, Offline
from macpacking.algorithms.online import FirstFit, BestFit, WorstFit, RefinedFirstFit
from macpacking.algorithms.offline import BenMaier, FirstFitDecreasing, BestFitDecreasing, WorstFitDecreasing

def test_first_fit():
    dataset = '_datasets/binpp/N1C3W2/N1C3W2_A.BPP.txt'
    reader = BinppReader(dataset)
    num_bins = 22
    oracle = [[21, 23, 94], [35, 100], [37, 27, 76], [38, 45, 61], [46, 32, 36, 30],
     [51, 52, 27], [56, 29, 23, 35], [60, 78], [65, 78], [70, 37, 29], [72], 
     [72, 37, 31], [75, 74], [80, 51], [83, 38, 28], [84], [88], [91], [91], [91, 48],
      [93, 32, 22], [96]]
    assert FirstFit(reader.online()) == oracle
    assert num_bins == len(FirstFit(reader.online()))

def test_best_fit():
    dataset = '_datasets/binpp/N1C3W2/N1C3W2_A.BPP.txt'
    reader = BinppReader(dataset)
    num_bins = 21
    oracle = [[21, 23, 94], [35, 100], [37, 27, 76], [38, 45, 61], [46, 32, 72],
     [51, 52, 27], [56, 29, 23, 35], [60, 78], [65, 78], [70, 37, 29], [72, 37, 31],
      [75, 74], [80, 51], [83, 38, 28], [84], [88], [91], [91, 36], [91, 48], 
      [93, 32, 22], [96, 30]]
    assert BestFit(reader.online()) == oracle
    assert num_bins == len(BestFit(reader.online()))

def test_worst_fit():
    dataset = '_datasets/binpp/N1C3W2/N1C3W2_A.BPP.txt'
    reader = BinppReader(dataset)
    num_bins = 22
    oracle = [[29, 38, 45, 29], [35, 37, 27, 32], [35, 100], [48, 83],
     [51, 52, 38], [60, 78], [61, 56, 23], [65, 78], [70, 37, 22], [72, 30],
      [72, 37, 32], [75, 74], [76, 21, 23], [80, 51], [84], [88], [91],
       [91, 27, 28], [91, 36], [93, 31], [94, 46], [96]]
    assert WorstFit(reader.online()) == oracle
    assert num_bins == len(WorstFit(reader.online()))

def test_rff():
    dataset = '_datasets/binpp/N1C3W2/N1C3W2_A.BPP.txt'
    reader = BinppReader(dataset)
    num_bins = 26
    oracle = [[27, 23, 46, 32], [27, 48, 38, 37], [29, 23, 35, 37, 21],
     [31, 32, 35, 28, 22], [36, 30], [37, 29, 38, 45], [51, 52], [56],
      [65, 72], [70, 61], [72], [75, 74], [76], [78], [78, 60], [80],
       [83], [84], [88], [91], [91], [91, 51], [93], [94], [96], [100]]
    assert RefinedFirstFit(reader.online()) == oracle
    assert num_bins == len(RefinedFirstFit(reader.online()))

def test_ben_maier():
    dataset = '_datasets/binpp/N1C3W2/N1C3W2_A.BPP.txt'
    reader = BinppReader(dataset)
    num_bins = 19
    oracle = [[27, 27, 23, 23, 22, 21], [31, 30, 29, 29, 28], [35, 35, 32, 32],
     [38, 37, 37, 36], [75, 38, 37], [76, 74], [78, 72], [78, 72], [80, 70],
      [83, 60], [84, 65], [88, 61], [91, 45], [91, 46], [91, 51], [93, 51],
       [94, 56], [96, 52], [100, 48]]
    assert BenMaier(reader.offline()) == oracle
    assert num_bins == len(BenMaier(reader.offline()))

def test_ffd():
    dataset = '_datasets/binpp/N1C3W2/N1C3W2_A.BPP.txt'
    reader = BinppReader(dataset)
    num_bins = 19
    oracle = [[27, 27, 23, 23, 22, 21], [31, 30, 29, 29, 28],
     [35, 35, 32, 32], [38, 37, 37, 36], [75, 38, 37], [76, 74], [78, 72],
      [78, 72], [80, 70], [83, 60], [84, 65], [88, 61], [91, 45], [91, 46], 
      [91, 51], [93, 51], [94, 56], [96, 52], [100, 48]]
    assert FirstFitDecreasing(reader.offline()) == oracle
    assert num_bins == len(FirstFitDecreasing(reader.offline()))
    
def test_bfd():
    dataset = '_datasets/binpp/N1C3W2/N1C3W2_A.BPP.txt'
    reader = BinppReader(dataset)
    num_bins = 19
    oracle = [[27, 27, 23, 23, 22, 21], [31, 30, 29, 29, 28],
     [35, 35, 32, 32], [38, 37, 37, 36], [75, 38, 37], [76, 74],
      [78, 72], [78, 72], [80, 70], [83, 60], [84, 65], [88, 61], 
      [91, 45], [91, 46], [91, 51], [93, 51], [94, 56], [96, 52], [100, 48]]
    assert BestFitDecreasing(reader.offline()) == oracle
    assert num_bins == len(BestFitDecreasing(reader.offline()))
