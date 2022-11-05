import csv
import codecs
from helpers import getListBasenames


def executionTimeOutput(output: str, binppBasenames: list[str], binppHardBasenames: list[str], jburkardtBasenames: list[str]):  # noqa: E501

    '''https://stackoverflow.com/questions/7894856/line-contains-null-byte-in-csv-reader-python'''  # noqa: E501
    csvReader = csv.reader(codecs.open(output, 'rU', 'utf-16'))

    binppDict = {}
    binppHardDict = {}
    jburkardtDict = {}

    binppBasenames = getListBasenames(binppBasenames)
    binppHardBasenames = getListBasenames(binppHardBasenames)
    jburkardtBasenames = getListBasenames(jburkardtBasenames)

    valueList = [i.pop(0) for i in csvReader]

    for i in valueList:
        array = i.split(": ")
        algorithmName, caseName, time = array[0], array[1], array[3]
        time = time.split("+-")[0]

        if time[-3:] == "us ":
            newTime = float(time[:-3])/1000
        else:
            newTime = float(time[:-3])

        if caseName in binppBasenames:
            if algorithmName not in binppDict:
                binppDict[algorithmName] = [newTime]
            else:
                binppDict[algorithmName].append(newTime)
        if caseName in binppHardBasenames:
            if algorithmName not in binppHardDict:
                binppHardDict[algorithmName] = [newTime]
            else:
                binppHardDict[algorithmName].append(newTime)
        if caseName in jburkardtBasenames:
            if algorithmName not in jburkardtDict:
                jburkardtDict[algorithmName] = [newTime]
            else:
                jburkardtDict[algorithmName].append(newTime)

    return (binppDict, binppHardDict, jburkardtDict)
