import csv
import sys
import inspect
from macpacking.reader import DatasetReader, JburkardtReader  # noqa: F401, E501
from helpers import className, getCaseName


class OracleReader():

    def __init__(self):
        '''Credit: https://stackoverflow.com/questions/1796180/how-can-i-get-a-list-of-all-classes-within-current-module-in-python'''  # noqa: E501
        #   This list comprehension returns a list of
        # all the classes defined within online.py.
        #   This effectively returns a list of all
        # defined Online algorithms, and adapts to the code.
        self.onlineClasses = [name for name, obj in inspect.getmembers(sys.modules['macpacking.algorithms.online'], inspect.isclass) if obj.__module__ == 'macpacking.algorithms.online']  # noqa: E501

    def oracleDictionaries(self, binppCSV, binppHardCSV, jburkardtCSV):

        #  returns dictionaries of 'optimal' output for each category
        #  based on oracle CSVs

        binppDict = {}
        binppHardDict = {}
        jburkardtDict = {}

        with open(binppCSV, 'r') as binppFile:
            self.readCSV(binppFile, binppDict)
        with open(binppHardCSV, 'r') as binppHardFile:
            self.readCSV(binppHardFile, binppHardDict)
        with open(jburkardtCSV, 'r') as jburkardtFile:
            self.readCSV(jburkardtFile, jburkardtDict)

        return (binppDict, binppHardDict, jburkardtDict)

    def readCSV(self, dataFile, dictionary: dict) -> None:

        csv_reader = csv.reader(dataFile)
        next(csv_reader)

        for row in csv_reader:
            dictionary[row[0]] = int(row[1])

    def readcases(self, cases: list[str], reader: DatasetReader, algorithm: list) -> dict:  # noqa: E501

        #  indexes length of each case solution
        #  by its case name for given algorithm

        solutionDict = {}

        for case in cases:
            if reader == JburkardtReader and case == './_datasets/jburkardt/_source.txt':  # noqa: E501
                continue
            else:
                name = getCaseName(case, reader)

            if algorithm in self.onlineClasses:
                data = reader(case).online()
            else:
                data = reader(case).offline()

            solution = algorithm(data)

            if name is not None:
                solutionDict[name] = len(solution)

        return solutionDict

    def binNumber(self, cases: list[str], reader: DatasetReader, algorithms: list, dictionary: dict, printOutput=True) -> dict:  # noqa: E501
        '''Compares output from solution using particular algorithm to
        the optimal solution from oracle.xlsx.
            Measures data as discrete and continuous margins.'''

        plotList = {}

        # Gathers optimal data from oracle files as 'baseline'
        oracleValueList = []
        oracleSolnList = self.readcases(cases, reader, algorithms[0])

        for case in oracleSolnList:
            oracleValueList.append(dictionary[case])

        plotList["Optimal"] = oracleValueList

        #  Gathers comparisons for each case using each algorithm
        # against oracle output
        for algorithm in algorithms:

            solutionDict = self.readcases(cases, reader, algorithm)
            outputList = []
            name = className(algorithm)

            for case in solutionDict:

                if printOutput:
                    difference = solutionDict[case] - dictionary[case]
                    algorithmName = className(algorithm)

                    if difference <= 0:
                        print(f"{case} using {algorithmName}: Optimal solution found.")  # noqa: E501
                    elif difference > 0:
                        print(f"{case} using {algorithmName}: Optimal solution is {difference} bins smaller.")  # noqa: E501

                # append each case solution
                outputList.append(solutionDict[case])

            # index each algorithm's output for each case by the algorithm name
            plotList[name] = outputList

        # returns dictionary in format that can be plotted by Plotter().
        return plotList
