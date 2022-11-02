from os import listdir
from os.path import isfile, join
from macpacking.reader import JburkardtReader

# HELPER FUNCTIONS
def list_case_files(dir: str) -> list[str]:
    return sorted([f'{dir}/{f}' for f in listdir(dir) if isfile(join(dir, f))])


def average(list, decimal) -> int:
    return round((sum(list) / len(list)), decimal)


def className(algorithm) -> str:
    return type(algorithm).__name__


def analyzeOutput(dict):
    for key in dict:
        avg = average(dict[key], 4)
        line = '{:<20} {:<10}'.format(key+":", avg)
        print(line)
    print("\n")


def readOnline(cases, reader, algorithm):
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


def readOffline(cases, reader, algorithm):
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