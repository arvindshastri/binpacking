import csv
import sys
import inspect
from macpacking.reader import DatasetReader, JburkardtReader  # noqa: F401, E501
from helpers import className, getCaseName


class OracleReader():

    def __init__(self):
        self.onlineClasses = [name for name, obj in inspect.getmembers(sys.modules['macpacking.algorithms.online'], inspect.isclass) if obj.__module__ == 'macpacking.algorithms.online']  # noqa: E501

    def readCSV(self, dataFile, dictionary: dict):
        csv_reader = csv.reader(dataFile)
        next(csv_reader)
        for row in csv_reader:
            dictionary[row[0]] = int(row[1])

    def readcases(self, cases: list[str], reader: DatasetReader, algorithm: list):  # noqa: E501
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

    def binNumber(self, cases: list[str], reader: DatasetReader, algorithms: list, dictionary: dict, printOutput=True):  # noqa: E501

        plotList = {}

        oracleValueList = []
        oracleSolnList = self.readcases(cases, reader, algorithms[0])
        for case in oracleSolnList:
            oracleValueList.append(dictionary[case])
        plotList["Optimal"] = oracleValueList

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

                outputList.append(solutionDict[case])

            plotList[name] = outputList

        return plotList
