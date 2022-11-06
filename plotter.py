from abc import ABC, abstractmethod
from macpacking.reader import DatasetReader
from helpers import getListCaseNames
import matplotlib.pyplot as plt


class Plotter(ABC):

    @abstractmethod
    def plot(self, plotList: dict, cases: list[str], reader: DatasetReader):
        pass


class ExecTimePlot(Plotter):

    def plot(self, plotList: dict, cases: list[str], reader: DatasetReader):  # noqa: E501

        plt.figure(figsize=(15, 5))  # set figure size
        caseNameList = getListCaseNames(cases, reader)  # get x-axis labels

        width = 0.1                                 # set bar width
        x = 0.1                                     # set separation of each bar on x-axis         # noqa: E501
        shiftList = []                              # set shifts on x-axis for each bar grouping   # noqa: E501
        values = list(range(len(caseNameList)))     # set how many bar groupings                   # noqa: E501
        algorithms = list(plotList.keys())          # set legend labels
        minimum = float('infinity')

        # find smallest value across all datasets
        # to collapse y-axis for plot readability
        for algorithm in plotList:
            minValue = min(plotList[algorithm])
            if minValue < minimum:
                minimum = minValue

        # alternative solution to numpy.arange()
        for i in range(1, (len(plotList) // 2) + 1):
            x = 0.1
            var = i*x
            shiftList.append(var)
            shiftList.append(var*(-1))

        shiftList.sort()
        middleIndex = len(shiftList)//2

        # determine optimal shifts on x-axis
        # based on even or odd bar grouping
        if len(plotList) % 2 != 0:
            shiftList.insert(middleIndex, 0)
        else:
            for i in range(middleIndex):
                shiftList[i] += x/2
            for i in range(middleIndex, len(shiftList)):
                shiftList[i] -= x/2

        # plot each key for each algorithm
        # plots in order of caseNames
        for count, key in enumerate(plotList):
            temp = shiftList[count]
            new_list = [x + temp for x in values]
            plt.bar(new_list, plotList[key], width=width)

        plt.xticks(values, caseNameList)
        plt.xlabel('Cases from Dataset')
        plt.ylabel('Execution Time (ms)')
        plt.ylim(bottom=minimum - minimum*0.1)
        plt.title('Algorithm Execution Time for Each Dataset')
        plt.legend(algorithms, loc="lower left", bbox_to_anchor=(1, 0.60))

        plt.show()


class BinNumberPlot(Plotter):

    def plot(self, plotList: dict, cases: list[str], reader: DatasetReader):  # noqa: E501

        plt.figure(figsize=(15, 5))  # set figure size
        caseNameList = getListCaseNames(cases, reader)  # get x-axis labels

        width = 0.1                                 # set bar width
        x = 0.1                                     # set separation of each bar on x-axis          # noqa: E501
        shiftList = []                              # set shifts on x-axis for each bar grouping    # noqa: E501
        values = list(range(len(caseNameList)))     # set how many bar groupings                    # noqa: E501
        algorithms = list(plotList.keys())          # set legend labels
        minimum = float('infinity')

        # find smallest value across all datasets
        # to collapse y-axis for plot readability
        for algorithm in plotList:
            minValue = min(plotList[algorithm])
            if minValue < minimum:
                minimum = minValue

        # alternative solution to numpy.arange()
        for i in range(1, (len(plotList) // 2) + 1):
            var = i*x
            shiftList.append(var)
            shiftList.append(var*(-1))

        shiftList.sort()
        middleIndex = len(shiftList)//2

        # determine optimal shifts on x-axis
        # based on even or odd bar grouping
        if len(plotList) % 2 != 0:
            shiftList.insert(middleIndex, 0)
        else:
            for i in range(middleIndex):
                shiftList[i] += x/2
            for i in range(middleIndex, len(shiftList)):
                shiftList[i] -= x/2

        # plot each key for each algorithm
        # plots in order of caseNames
        for count, key in enumerate(plotList):
            if count == 0:
                temp = shiftList[count]
                new_list = [x + temp for x in values]
                plt.bar(new_list, plotList[key], width=width, color='black')
            else:
                temp = shiftList[count]
                new_list = [x + temp for x in values]
                plt.bar(new_list, plotList[key], width=width)

        plt.xticks(values, caseNameList)
        plt.xlabel('Cases from Dataset')
        plt.ylabel('Number of Bins in Optimal Solution')
        plt.title('Output of Algorithms Compared to Optimal for Each Case')
        plt.ylim(bottom=minimum - minimum*0.1)
        plt.legend(algorithms, loc="lower left", bbox_to_anchor=(1, 0.60))

        plt.show()
