import csv
import sys
import inspect
from os.path import basename
from macpacking.reader import DatasetReader, BinppReader, JburkardtReader  # noqa: F401, E501
from macpacking.algorithms.online import \
    FirstFit, BestFit, WorstFit
from macpacking.algorithms.offline import \
    FirstFitDecreasing, BestFitDecreasing, WorstFitDecreasing, BenMaier
from sample_bench import list_case_files, className

binppCSV = './_datasets/binpp.csv'
binppHardCSV = './_datasets/binpp-hard.csv'
jburkardtCSV = './_datasets/jburkardt.csv'

binppDict = {}
binppHardDict = {}
jburkardtDict = {}


def readCSV(dataFile, dictionary: dict):
    csv_reader = csv.reader(dataFile)
    next(csv_reader)
    for row in csv_reader:
        dictionary[row[0]] = int(row[1])


with open(binppCSV, 'r') as binppFile:
    readCSV(binppFile, binppDict)
with open(binppHardCSV, 'r') as binppHardFile:
    readCSV(binppHardFile, binppHardDict)
with open(jburkardtCSV, 'r') as jburkardtFile:
    readCSV(jburkardtFile, jburkardtDict)


onlineClasses = [name for name, obj in inspect.getmembers(sys.modules['macpacking.algorithms.online'], inspect.isclass) if obj.__module__ == 'macpacking.algorithms.online']  # noqa: E501


def readcases(cases: list[str], reader: DatasetReader, algorithm: list):
    solutionDict = {}

    for case in cases:

        name = basename(case).replace(".BPP.txt", "")
        lastLetter = case.replace(".txt", "")[-1]
        if reader == JburkardtReader:
            if lastLetter != 'c':
                continue
            else:
                separator = "_"
                stripped = basename(case).split(separator, 1)[0]
                name = stripped[:1] + separator + stripped[1:]

        if algorithm in onlineClasses:
            data = reader(case).online()
        else:
            data = reader(case).offline()

        solution = algorithm(data)
        solutionDict[name] = len(solution)

    return solutionDict


def binNumber(cases: list[str], reader: DatasetReader, algorithm: list, dictionary: dict, print=True):  # noqa: E501

    solutionDict = readcases(cases, reader, algorithm)
    outputList = []

    for key in solutionDict:
        if print:
            difference = solutionDict[key] - dictionary[key]
            if difference == 0:
                print(f"{key} using {className(algorithm)}: Optimal solution found.")  # noqa: E501
            elif difference > 0:
                print(f"{key} using {className(algorithm)}: Optimal solution is {difference} bins smaller.")  # noqa: E501

        outputList.append(solutionDict[key])

    return outputList


def main():

    CASES = './_datasets/jburkardt'
    reader = JburkardtReader
    cases = list_case_files(CASES)
    algorithms = [BenMaier(), FirstFit(), BestFit(), WorstFit(), FirstFitDecreasing(), BestFitDecreasing(), WorstFitDecreasing()]  # noqa: E501
    dictionary = binppHardDict
    print = False

    plotList = []

    for algorithm in algorithms:
        plotList.append(binNumber(cases, reader, algorithm, dictionary, print))

    print(plotList)


if __name__ == "__main__":
    main()
