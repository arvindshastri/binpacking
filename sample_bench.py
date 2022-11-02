import sys
import inspect
import pyperf
from os import listdir
from os.path import isfile, join, basename
from macpacking.reader import DatasetReader, BinppReader, JburkardtReader
from macpacking.model import Online
from macpacking.algorithms.online import \
    FirstFit, BestFit, WorstFit
from macpacking.algorithms.offline import \
    FirstFitDecreasing, BestFitDecreasing, WorstFitDecreasing, BenMaier


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

    algorithms = [BenMaier(), FirstFit(), BestFit(), WorstFit(), FirstFitDecreasing(), BestFitDecreasing(), WorstFitDecreasing()]  # noqa: E501

    # runner = pyperf.Runner()
    # execTime(binppCases, BinppReader, algorithms, runner)
    # execTime(listOfBinppHardCases, BinppReader, algorithms, runner)
    # execTime(listOfJburkardtCases, JburkardtReader, algorithms, runner)

    ######

    CASES = './_datasets/binpp/N1C1W1'
    cases = list_case_files(CASES)
    
    print("Analysis of Average Bin Usage as Percentage")
    print("─" * 25)
    resultList = analyzePercentage(cases, BinppReader, algorithms)
    analyzeOutput(resultList)

    # print("Analysis of Average Remaining Space")
    # print("─" * 25)
    # spaceBench(cases, BinppReader, algorithms)

    # print("Analysis of Average Bins")
    # print("─" * 25)
    # numberBins(cases, BinppReader, algorithms)


# HELPER FUNCTIONS
def list_case_files(dir: str) -> list[str]:
    return sorted([f'{dir}/{f}' for f in listdir(dir) if isfile(join(dir, f))])


def average(list, decimal):
    return round((sum(list) / len(list)), decimal)


def className(algorithm):
    return type(algorithm).__name__


def printOutput(list):
    print(*list.keys(), sep="\t")
    for row in zip(*list.values()):
        print(*row, sep="\t\t")


def analyzeOutput(dict):
    for key in dict:
        avg = average(dict[key], 4)
        line = '{:<20} {:<10}'.format(key+":", avg)
        print(line)
    print("\n")


def readOnline(cases, reader, algorithm):
    solutionList = []
    capacity = 0
    for case in cases:
        lastLetter = case.replace(".txt", "")[-1]
        if reader == JburkardtReader and lastLetter != 'c':
            continue
        data = reader(case).online()
        capacity = data[0]
        solution = algorithm(data)
        solutionList.append(solution)

    return (solutionList, capacity)


def readOffline(cases, reader, algorithm):
    solutionList = []
    capacity = 0
    for case in cases:
        lastLetter = case.replace(".txt", "")[-1]
        if reader == JburkardtReader and lastLetter != 'c':
            continue
        data = reader(case).offline()
        capacity = data[0]
        solution = algorithm(data)
        solutionList.append(solution)

    return (solutionList, capacity)


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


# ANALYZE PERCENTAGE USAGE
def analyzePercentage(cases: list[str], reader: DatasetReader, algorithms: list):  # noqa: E501

    resultList = {}

    for algorithm in algorithms:
        averageUsage = []
        capacity = 0

        if algorithm in onlineClasses:
            solutionList, capacity = readOnline(cases, reader, algorithm)
        else:
            solutionList, capacity = readOffline(cases, reader, algorithm)

        for solution in solutionList:
            binUsage = []

            for bin in solution:
                percentUsed = sum(bin) / capacity * 100
                binUsage.append(percentUsed)

            avg = average(binUsage, 4)
            averageUsage.append(avg)

        resultList[className(algorithm)] = averageUsage

    return resultList


# ANALYZE REMAINING SPACE
def spaceBench(cases: list[str], reader: DatasetReader, algorithms: list):

    resultList = {}

    for algorithm in algorithms:
        averageRemainingSpace = []
        capacity = 0

        if algorithm in onlineClasses:
            solutionList, capacity = readOnline(cases, reader, algorithm)
        else:
            solutionList, capacity = readOffline(cases, reader, algorithm)

        for solution in solutionList:
            remainingSpace = []

            for bin in solution:
                remaining = capacity - sum(bin)
                remainingSpace.append(remaining)

            avg = average(remainingSpace, 2)
            averageRemainingSpace.append(avg)

        resultList[className(algorithm)] = averageRemainingSpace

    analyzeOutput(resultList)

    return resultList


def numberBins(cases: list[str], reader: DatasetReader, algorithms: list):

    resultList = {}

    for algorithm in algorithms:
        averageBins = []

        if algorithm in onlineClasses:
            solutionList, capacity = readOnline(cases, reader, algorithm)
        else:
            solutionList, capacity = readOffline(cases, reader, algorithm)

        for solution in solutionList:
            averageBins.append(len(solution))

        resultList[className(algorithm)] = averageBins

    analyzeOutput(resultList)

    return resultList


if __name__ == "__main__":
    main()
