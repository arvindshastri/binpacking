import sys
import inspect
import pyperf
from os import listdir
from os.path import isfile, join, basename
from macpacking.reader import DatasetReader, BinppReader
from macpacking.model import Online
from macpacking.algorithms.online import \
    FirstFit, BestFit, WorstFit
from macpacking.algorithms.offline import \
    FirstFitDecreasing, BestFitDecreasing, WorstFitDecreasing, BenMaier


CASES = './_datasets/binpp/N1C1W1'

'''Credit: https://stackoverflow.com/questions/1796180/how-can-i-get-a-list-of-all-classes-within-current-module-in-python'''  # noqa: E501
onlineClasses = [name for name, obj in inspect.getmembers(sys.modules['macpacking.algorithms.online'], inspect.isclass) if obj.__module__ == 'macpacking.algorithms.online']  # noqa: E501


def main():
    cases = list_case_files(CASES)

    algorithms = [BenMaier(), FirstFit(), BestFit(), WorstFit(), FirstFitDecreasing(), BestFitDecreasing(), WorstFitDecreasing()]  # noqa: E501
    
    print("Analysis of Average Bin Usage as Percentage")
    print("─" * 25)
    analyzePercentage(cases, BinppReader, algorithms)

    print("Analysis of Average Remaining Space")
    print("─" * 25)
    spaceBench(cases, BinppReader, algorithms)

    print("Analysis of Average Bins")
    print("─" * 25)
    numberBins(cases, BinppReader, algorithms)


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
        data = reader(case).online()
        capacity = data[0]
        solution = algorithm(data)
        solutionList.append(solution)

    return (solutionList, capacity)


def readOffline(cases, reader, algorithm):
    solutionList = []
    capacity = 0
    for case in cases:
        data = reader(case).offline()
        capacity = data[0]
        solution = algorithm(data)
        solutionList.append(solution)

    return (solutionList, capacity)


# RUNTIME BENCHMARKS
def execTimeBench(cases: list[str], reader: DatasetReader, algorithm: Online):  # noqa: E501
    runner = pyperf.Runner()
    for case in cases:
        name = basename(case)
        data = reader(case).online()
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

    analyzeOutput(resultList)

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
