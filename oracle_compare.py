import csv
import pprint
from os.path import basename
from macpacking.reader import DatasetReader, BinppReader
from macpacking.model import Online, Offline
from macpacking.algorithms.online import \
    FirstFit, BestFit, WorstFit
from macpacking.algorithms.offline import \
    FirstFitDecreasing, BestFitDecreasing, WorstFitDecreasing, BenMaier
from sample_bench import list_case_files, readOnline, readOffline, numberBins

binppCSV = './_datasets/binpp.csv'
binppHardCSV = './_datasets/binpp-hard.csv'
jburkardtCSV = './_datasets/jburkardt.csv'

binppDict = {}
binppHardDict = {}
jburkardtDict = {}

def readCSV(dataFile, dictionary):
    csv_reader = csv.reader(dataFile)
    next(csv_reader)   
    for row in csv_reader:
        dictionary[row[0]] = row[1]  

with open(binppCSV, 'r') as binppFile:
    readCSV(binppFile, binppDict)
with open(binppHardCSV, 'r') as binppHardFile:
    readCSV(binppHardFile, binppHardDict)
with open(jburkardtCSV, 'r') as jburkardtFile:
    readCSV(jburkardtFile, jburkardtDict)

pprint.pprint(binppDict)

# CASES = './_datasets/binpp/N1C1W1'
# reader = BinppReader
# cases = list_case_files(CASES)
# algorithms = [BenMaier(), FirstFit(), BestFit(), WorstFit(), FirstFitDecreasing(), BestFitDecreasing(), WorstFitDecreasing()]  # noqa: E501

# resultList = numberBins(cases, reader, algorithms)
# print(resultList)

# reader: DatasetReader = BinppReader(filename)
# name = basename(filename).replace(".BPP.txt", "")
# strategy: Offline = BestFit()
# result = strategy(reader.online())




