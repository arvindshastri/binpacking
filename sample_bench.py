import sys
import inspect
import pyperf
from os.path import basename
from macpacking.reader import DatasetReader, JburkardtReader
from helpers import analyzeOutput, average, className, readOffline, readOnline


'''Credit: https://stackoverflow.com/questions/1796180/how-can-i-get-a-list-of-all-classes-within-current-module-in-python'''  # noqa: E501
onlineClasses = [name for name, obj in inspect.getmembers(sys.modules['macpacking.algorithms.online'], inspect.isclass) if obj.__module__ == 'macpacking.algorithms.online']  # noqa: E501


class Benchmark():

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
    def binUsage(self, cases: list[str], reader: DatasetReader, algorithms: list):  # noqa: E501

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
        # return resultList


    # ANALYZE AVERAGE REMAINING SPACE
    def remainingSpace(self, cases: list[str], reader: DatasetReader, algorithms: list):

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

        # return resultList


    # ANALYZE AVERAGE NUMBER OF BINS
    def numberBins(self, cases: list[str], reader: DatasetReader, algorithms: list):

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

        # return resultList


    # ANALYZE AVERAGE NUMBER OF BIN COMPARISONS
    def numberComparisons(self, cases: list[str], reader: DatasetReader, algorithms: list):  # noqa: E501

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

        # return resultList
