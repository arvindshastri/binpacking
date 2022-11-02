import sys
import inspect
import pyperf
from os import listdir
from os.path import isfile, join, basename
from macpacking.reader import DatasetReader, BinppReader, JburkardtReader
from macpacking.algorithms.online import \
    FirstFit, BestFit, WorstFit
from macpacking.algorithms.offline import \
    FirstFitDecreasing, BestFitDecreasing, WorstFitDecreasing


'''Credit: https://stackoverflow.com/questions/1796180/how-can-i-get-a-list-of-all-classes-within-current-module-in-python'''  # noqa: E501
onlineClasses = [name for name, obj in inspect.getmembers(sys.modules['macpacking.algorithms.online'], inspect.isclass) if obj.__module__ == 'macpacking.algorithms.online']  # noqa: E501


def main():

    # binppCases = [
    #     './_datasets/binpp/N1C1W1/N1C1W1_A.BPP.txt',
    #     './_datasets/binpp/N1C3W4/N1C3W4_A.BPP.txt',
    #     './_datasets/binpp/N2C1W1/N2C1W1_A.BPP.txt',
    #     './_datasets/binpp/N2C3W4/N2C3W4_A.BPP.txt',
    #     './_datasets/binpp/N3C1W1/N3C1W1_A.BPP.txt',
    #     './_datasets/binpp/N3C3W4/N3C3W4_A.BPP.txt',
    #     './_datasets/binpp/N4C1W1/N4C1W1_A.BPP.txt',
    #     './_datasets/binpp/N4C3W4/N4C3W4_A.BPP.txt'
    # ]

    # binppHardCases = './_datasets/binpp-hard'
    # jburkardtCases = './_datasets/jburkardt'
    # listOfBinppHardCases = list_case_files(binppHardCases)
    # listOfJburkardtCases = list_case_files(jburkardtCases)

    algorithms = [FirstFit(), BestFit(), WorstFit(), FirstFitDecreasing(), BestFitDecreasing(), WorstFitDecreasing()]  # noqa: E501

    # runner = pyperf.Runner()
    # execTime(binppCases, BinppReader, algorithms, runner)
    # execTime(listOfBinppHardCases, BinppReader, algorithms, runner)
    # execTime(listOfJburkardtCases, JburkardtReader, algorithms, runner)

    ######

    CASES = './_datasets/binpp/N1C1W1'
    cases = list_case_files(CASES)

    print("Analysis of Average Bin Usage as Percentage")
    print("─" * 43)
    binUsage(cases, BinppReader, algorithms)

    print("Analysis of Average Remaining Space")
    print("─" * 35)
    remainingSpace(cases, BinppReader, algorithms)

    print("Analysis of Average Bins")
    print("─" * 24)
    numberBins(cases, BinppReader, algorithms)

    print("Analysis of Average Comparisons")
    print("─" * 31)
    numberComparisons(cases, BinppReader, algorithms)


# HELPER FUNCTIONS
def list_case_files(dir: str) -> list[str]:
    return sorted([f'{dir}/{f}' for f in listdir(dir) if isfile(join(dir, f))])


def average(list, decimal):
    return round((sum(list) / len(list)), decimal)


def className(algorithm):
    return type(algorithm).__name__


def analyzeOutput(dict):
    for key in dict:
        avg = average(dict[key], 4)
        line = '{:<20} {:<10}'.format(key+":", avg)
        print(line)
    print("\n")


def readOnline(cases, reader, algorithm):
    solutionList = []
    capacity = 0
    comparisons = []

    for case in cases:
        lastLetter = case.replace(".txt", "")[-1]
        if reader == JburkardtReader and lastLetter != 'c':
            continue
        data = reader(case).online()
        capacity = data[0]
        solution = algorithm(data)
        comparisons.append(algorithm.comparisons)
        solutionList.append(solution)

    return (solutionList, capacity, comparisons)


def readOffline(cases, reader, algorithm):
    solutionList = []
    capacity = 0
    comparisons = []

    for case in cases:
        lastLetter = case.replace(".txt", "")[-1]
        if reader == JburkardtReader and lastLetter != 'c':
            continue
        data = reader(case).offline()
        capacity = data[0]
        solution = algorithm(data)
        comparisons.append(algorithm.comparisons)
        solutionList.append(solution)

    return (solutionList, capacity, comparisons)


# RUNTIME BENCHMARK
def execTime(cases: list[str], reader: DatasetReader, algorithms: list, runner):  # noqa: E501

    for algorithm in algorithms:
        for case in cases:
            lastLetter = case.replace(".txt", "")[-1]
            if reader == JburkardtReader and lastLetter != 'c':
                continue

            name = basename(case)

            if algorithm in onlineClasses:
                data = reader(case).online()
            else:
                data = reader(case).offline()

            runner.bench_func(name, algorithm, data)


# ANALYZE AVERAGE PERCENTAGE USAGE
def binUsage(cases: list[str], reader: DatasetReader, algorithms: list):  # noqa: E501

    resultList = {}

    for algorithm in algorithms:
        averageUsage = []
        capacity = 0

        if algorithm in onlineClasses:
            data = readOnline(cases, reader, algorithm)
        else:
            data = readOffline(cases, reader, algorithm)

        solutionList = data[0]
        capacity = data[1]

        for solution in solutionList:
            binUsage = []

            for bin in solution:
                percentUsed = sum(bin) / capacity * 100
                binUsage.append(percentUsed)

            avg = average(binUsage, 4)
            averageUsage.append(avg)

        resultList[className(algorithm)] = averageUsage

    analyzeOutput(resultList)

    return resultList


# ANALYZE AVERAGE REMAINING SPACE
def remainingSpace(cases: list[str], reader: DatasetReader, algorithms: list):

    resultList = {}

    for algorithm in algorithms:
        averageRemainingSpace = []
        capacity = 0

        if algorithm in onlineClasses:
            data = readOnline(cases, reader, algorithm)
        else:
            data = readOffline(cases, reader, algorithm)

        solutionList = data[0]
        capacity = data[1]

        for solution in solutionList:
            remainingSpace = []

            for bin in solution:
                remaining = capacity - sum(bin)
                remainingSpace.append(remaining)

            avg = average(remainingSpace, 4)
            averageRemainingSpace.append(avg)

        resultList[className(algorithm)] = averageRemainingSpace

    analyzeOutput(resultList)

    return resultList


# ANALYZE AVERAGE NUMBER OF BINS
def numberBins(cases: list[str], reader: DatasetReader, algorithms: list):

    resultList = {}

    for algorithm in algorithms:
        averageBins = []

        if algorithm in onlineClasses:
            data = readOnline(cases, reader, algorithm)
        else:
            data = readOffline(cases, reader, algorithm)

        solutionList = data[0]

        for solution in solutionList:
            averageBins.append(len(solution))

        resultList[className(algorithm)] = averageBins

    analyzeOutput(resultList)

    return resultList


# ANALYZE AVERAGE NUMBER OF BIN COMPARISONS
def numberComparisons(cases: list[str], reader: DatasetReader, algorithms: list):  # noqa: E501

    resultList = {}

    for algorithm in algorithms:

        averageComparison = []

        if algorithm in onlineClasses:
            data = readOnline(cases, reader, algorithm)
        else:
            data = readOffline(cases, reader, algorithm)

        comparisons = data[2]

        for comparison in comparisons:
            averageComparison.append(comparison)

        resultList[className(algorithm)] = averageComparison

    analyzeOutput(resultList)

    return resultList


if __name__ == "__main__":
    main()
