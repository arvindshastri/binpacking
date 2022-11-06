from os import listdir
from os.path import isfile, join, basename
from macpacking.reader import DatasetReader, JburkardtReader


# HELPER FUNCTIONS
def list_case_files(dir: str) -> list[str]:
    return sorted([f'{dir}/{f}' for f in listdir(dir) if isfile(join(dir, f))])


def average(list: list[int], decimal: int) -> int:
    return round((sum(list) / len(list)), decimal)


def className(algorithm) -> str:
    return type(algorithm).__name__


def analyzeOutput(dict: dict) -> None:
    for key in dict:
        avg = average(dict[key], 4)
        line = '{:<20} {:<10}'.format(key+":", avg)
        print(line)
    print("\n")


def readOnline(cases: list[str], reader: DatasetReader, algorithm):
    solutionList = []
    capacity = 0
    comparisons = []

    for case in cases:
        lastLetter = case.replace(".txt", "")[-1]
        if reader == JburkardtReader and lastLetter != 'c':
            continue
        data = reader(case).online()
        capacity = data[0]
        solution = algorithm(data)
        comparisons.append(algorithm.comparisons)
        solutionList.append(solution)

    return (solutionList, capacity, comparisons)


def readOffline(cases: list[str], reader: DatasetReader, algorithm):
    solutionList = []
    capacity = 0
    comparisons = []

    for case in cases:
        lastLetter = case.replace(".txt", "")[-1]
        if reader == JburkardtReader and lastLetter != 'c':
            continue
        data = reader(case).offline()
        capacity = data[0]
        solution = algorithm(data)
        comparisons.append(algorithm.comparisons)
        solutionList.append(solution)

    return (solutionList, capacity, comparisons)


def getCaseName(case: list[str], reader: DatasetReader) -> str:
    name = basename(case).replace(".BPP.txt", "")
    lastLetter = case.replace(".txt", "")[-1]
    if reader == JburkardtReader:
        if lastLetter == 'c':
            separator = "_"
            stripped = basename(case).split(separator, 1)[0]
            name = stripped[:1] + separator + stripped[1:]
        else:
            name = None

    return name


def getListCaseNames(cases: list[str], reader: DatasetReader) -> list[str]:

    listCaseNames = []

    for case in cases:
        if reader == JburkardtReader and case == './_datasets/jburkardt/_source.txt':  # noqa: E501
            continue
        else:
            name = getCaseName(case, reader)
            if name is not None:
                listCaseNames.append(name)

    return listCaseNames


def getListBasenames(listOfCases: list[str]) -> list[str]:

    output = []

    for case in listOfCases:
        output.append(basename(case))

    return output
