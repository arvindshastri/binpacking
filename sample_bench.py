import sys
import inspect
from os.path import basename
from macpacking.reader import DatasetReader, JburkardtReader
from helpers import printOutput, average, className, readOffline, readOnline


class Benchmark():

    def __init__(self):
        '''Credit: https://stackoverflow.com/questions/1796180/how-can-i-get-a-list-of-all-classes-within-current-module-in-python'''  # noqa: E501
        #  This list comprehension returns a list of all the classes defined within online.py.    # noqa: E501
        #  This effectively returns a list of all defined Online algorithms, and adapts to the code.    # noqa: E501
        self.onlineClasses = [name for name, obj in inspect.getmembers(sys.modules['macpacking.algorithms.online'], inspect.isclass) if obj.__module__ == 'macpacking.algorithms.online']  # noqa: E501

    # RUNTIME BENCHMARK
    def execTime(self, cases: list[str], reader: DatasetReader, algorithms: list, runner):  # noqa: E501
        '''Output the benchmark time for
        each case using each given algorithm'''

        for algorithm in algorithms:
            for case in cases:

                #  business logic for generating case names for each benchmark
                lastLetter = case.replace(".txt", "")[-1]
                if reader == JburkardtReader and lastLetter != 'c':
                    continue

                algorithmName = className(algorithm)
                name = f"{algorithmName}: {basename(case)}"

                #  gather data based on class
                if algorithm in self.onlineClasses:
                    data = reader(case).online()
                else:
                    data = reader(case).offline()

                runner.bench_func(name, algorithm, data)

    # ANALYZE AVERAGE PERCENTAGE USAGE
    def binUsage(self, cases: list[str], reader: DatasetReader, algorithms: list):  # noqa: E501
        '''Output the average percentage usage of
        each solution for each given algorithm'''

        resultList = {}

        for algorithm in algorithms:
            averageUsage = []

            if algorithm in self.onlineClasses:
                data = readOnline(cases, reader, algorithm)
            else:
                data = readOffline(cases, reader, algorithm)

            #  Retrieve data
            solutionList = data[0]
            capacity = data[1]

            for solution in solutionList:
                binUsage = []

                #  Average the bin usage as a percentage
                for bin in solution:
                    percentUsed = sum(bin) / capacity * 100
                    binUsage.append(percentUsed)

                avg = average(binUsage, 4)
                averageUsage.append(avg)

            # Append the total average using the algorithm as a key
            resultList[className(algorithm)] = average(averageUsage, 4)

        printOutput(resultList)

    # ANALYZE AVERAGE REMAINING SPACE
    def remainingSpace(self, cases: list[str], reader: DatasetReader, algorithms: list):  # noqa: E501
        '''Output the average remaining bin space
        of each solution for each given algorithm'''

        resultList = {}

        for algorithm in algorithms:
            averageRemainingSpace = []

            if algorithm in self.onlineClasses:
                data = readOnline(cases, reader, algorithm)
            else:
                data = readOffline(cases, reader, algorithm)

            #  Retrieve data
            solutionList = data[0]
            capacity = data[1]

            for solution in solutionList:
                remainingSpace = []

                #  Average the remaining space for each bin
                for bin in solution:
                    remaining = capacity - sum(bin)
                    remainingSpace.append(remaining)

                avg = average(remainingSpace, 4)
                averageRemainingSpace.append(avg)

            # Append the total average using the algorithm as a key
            resultList[className(algorithm)] = average(averageRemainingSpace, 4)   # noqa: E501

        printOutput(resultList)

    # ANALYZE AVERAGE NUMBER OF BINS
    def numberBins(self, cases: list[str], reader: DatasetReader, algorithms: list):  # noqa: E501
        '''Output the average number of bins for
        each solution for each given algorithm'''

        resultList = {}

        for algorithm in algorithms:
            averageBins = []

            if algorithm in self.onlineClasses:
                data = readOnline(cases, reader, algorithm)
            else:
                data = readOffline(cases, reader, algorithm)

            #  Retrieve data
            solutionList = data[0]

            #  Append length (number of bins) of each solution
            for solution in solutionList:
                averageBins.append(len(solution))

            # Append the total average using the algorithm as a key
            resultList[className(algorithm)] = average(averageBins, 4)

        printOutput(resultList)

    # ANALYZE AVERAGE NUMBER OF BIN COMPARISONS
    def numberComparisons(self, cases: list[str], reader: DatasetReader, algorithms: list):  # noqa: E501
        '''Output the average number of comparisons
        made to the solution list of each solution
        for each given algorithm'''

        resultList = {}

        for algorithm in algorithms:

            averageComparison = []

            if algorithm in self.onlineClasses:
                data = readOnline(cases, reader, algorithm)
            else:
                data = readOffline(cases, reader, algorithm)

            #  Retrieve data
            comparisons = data[2]

            #  Append number of comparisons
            # (from algorihm object) of each solution
            for comparison in comparisons:
                averageComparison.append(comparison)

            # Append the total average using the algorithm as a key
            resultList[className(algorithm)] = average(averageComparison, 4)

        printOutput(resultList)
