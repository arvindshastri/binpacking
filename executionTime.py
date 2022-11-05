import pyperf
from sample_bench import Benchmark
from macpacking.reader import BinppReader, JburkardtReader
from macpacking.algorithms.online import \
    FirstFit, BestFit, WorstFit
from macpacking.algorithms.offline import \
    FirstFitDecreasing, BestFitDecreasing, WorstFitDecreasing
from helpers import list_case_files


listOfBinppCases = [
    './_datasets/binpp/N1C1W1/N1C1W1_A.BPP.txt',
    './_datasets/binpp/N1C3W4/N1C3W4_A.BPP.txt',
    './_datasets/binpp/N2C1W1/N2C1W1_A.BPP.txt',
    './_datasets/binpp/N2C3W4/N2C3W4_A.BPP.txt',
    './_datasets/binpp/N3C1W1/N3C1W1_A.BPP.txt',
    './_datasets/binpp/N3C3W4/N3C3W4_A.BPP.txt',
    './_datasets/binpp/N4C1W1/N4C1W1_A.BPP.txt',
    './_datasets/binpp/N4C3W4/N4C3W4_A.BPP.txt'
]

binppHardCases = './_datasets/binpp-hard'
jburkardtCases = './_datasets/jburkardt'
listOfBinppHardCases = list_case_files(binppHardCases)
listOfJburkardtCases = list_case_files(jburkardtCases)


def main():

    algorithms = [FirstFit(), BestFit(), WorstFit(), FirstFitDecreasing(), BestFitDecreasing(), WorstFitDecreasing()]  # noqa: E501

    runner = pyperf.Runner()
    benchmark = Benchmark()
    benchmark.execTime(listOfBinppCases, BinppReader, algorithms, runner)
    benchmark.execTime(listOfBinppHardCases, BinppReader, algorithms, runner)
    benchmark.execTime(listOfJburkardtCases, JburkardtReader, algorithms, runner)  # noqa: E501


if __name__ == "__main__":
    main()
