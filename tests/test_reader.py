from macpacking.reader import DatasetReader, BinppReader, JburkardtReader


def test_binpp_reader():
    dataset = '_datasets/binpp/N1C1W1/N1C1W1_B.BPP.txt'
    capacity = 100
    oracle = [
        8, 8, 12, 13, 13, 14, 15, 17, 18, 19, 20, 23, 30, 37, 37, 39, 40,
        43, 43, 44, 44, 50, 51, 61, 61, 62, 62, 63, 66, 67, 69, 70, 71,
        72, 75, 76, 76, 79, 83, 83, 88, 92, 92, 93, 93, 97, 97, 97, 99, 100
    ]
    reader: DatasetReader = BinppReader(dataset)
    assert capacity == reader.offline()[0]
    assert oracle == sorted(reader.offline()[1])

def test_jburkardt_reader():
    dataset = '_datasets/binpp/N1C1W2/N1C1W2_A.BPP.txt'
    capacity = 50
    oracle = [
        96, 93, 86, 86, 85, 83, 80, 80, 80, 79, 77, 68, 67,
        64, 64, 63, 60, 57, 55, 54, 54, 54, 54, 52, 52, 52,
        51, 44, 43, 41, 41, 39, 39, 39, 38, 36, 36, 35, 34, 
        34, 31, 31, 29, 29, 28, 24, 23, 22,22, 20
    ]
    reader: DatasetReader = JburkardtReader(dataset)
    assert capacity == reader.offline()[0]
    assert oracle == sorted(reader.offline()[1])
