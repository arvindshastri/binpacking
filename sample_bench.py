import pyperf
from os import listdir
from os.path import isfile, join, basename
from macpacking.algorithms.nextfit_online import NextFit
from macpacking.algorithms.bestfit import BestFit
from macpacking.reader import BinppReader


# We consider:
#   - 500 objects (N4)
#   - bin capacity of 120 (C2)
#   - and weight in the [20,100] interval (W2)
CASES = './_datasets/binpp/N4C2W2'


def main():
    '''Example of benchmark code'''
    cases = list_case_files(CASES)
    run_bench_time(cases)


def list_case_files(dir: str) -> list[str]:
    return sorted([f'{dir}/{f}' for f in listdir(dir) if isfile(join(dir, f))])


def run_bench(cases: list[str]):
    runner = pyperf.Runner()
    for case in cases:
        name = basename(case)
        data = BinppReader(case).online()
        binpacker = NextFit()
        runner.bench_func(name, binpacker, data)

def run_bench_time(cases: list[str]):
    runner = pyperf.Runner()
    for case in cases:
        name = basename(case)
        data = BinppReader(case).online()
        binpacker = BestFit()
        runner.bench_func(name, binpacker, data)


if __name__ == "__main__":
    main()
