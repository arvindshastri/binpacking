import csv
import sys
import inspect
from os.path import basename
from macpacking.reader import DatasetReader, BinppReader, JburkardtReader  # noqa: F401, E501
from macpacking.algorithms.online import \
    FirstFit, BestFit, WorstFit
from macpacking.algorithms.offline import \
    FirstFitDecreasing, BestFitDecreasing, WorstFitDecreasing, BenMaier
from helpers import list_case_files, className, getCaseName

onlineClasses = [name for name, obj in inspect.getmembers(sys.modules['macpacking.algorithms.online'], inspect.isclass) if obj.__module__ == 'macpacking.algorithms.online']  # noqa: E501


class OracleReader():

    def readCSV(self, dataFile, dictionary: dict):
        csv_reader = csv.reader(dataFile)
        next(csv_reader)
        for row in csv_reader:
            dictionary[row[0]] = int(row[1])


    def readcases(self, cases: list[str], reader: DatasetReader, algorithm: list):
        solutionDict = {}

        for case in cases:

            if reader == JburkardtReader and case == './_datasets/jburkardt/_source.txt':
                continue
            else:           
                name = getCaseName(case, reader)

            if algorithm in onlineClasses:
                data = reader(case).online()
            else:
                data = reader(case).offline()

            solution = algorithm(data)

            if name != None:
                solutionDict[name] = len(solution)

        return solutionDict


    def binNumber(self, cases: list[str], reader: DatasetReader, algorithms: list, dictionary: dict, printed=True):  # noqa: E501

        plotList = {}

        for algorithm in algorithms:

            solutionDict = self.readcases(cases, reader, algorithm)
            outputList = []
            name = className(algorithm)

            for key in solutionDict:
                if printed:
                    difference = solutionDict[key] - dictionary[key]
                    algorithmName = className(algorithm)
                    if difference <= 0:
                        print(f"{key} using {algorithmName}: Optimal solution found.")  # noqa: E501
                    elif difference > 0:
                        print(f"{key} using {algorithmName}: Optimal solution is {difference} bins smaller.")  # noqa: E501

                outputList.append(solutionDict[key])
            
            plotList[name] = outputList

        return plotList
