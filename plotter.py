import matplotlib.pyplot as plt


class Plotter():

    
    def execTimePlot(self, plotList, caseNameList):

        plt.figure(figsize=(15, 5))

        width = 0.1
        shiftList = []
        values = list(range(len(caseNameList)))
        minimum = float('infinity')
        algorithms = list(plotList.keys())

        for algorithm in plotList:
            minValue = min(plotList[algorithm])
            if minValue < minimum:
                minimum = minValue

        for i in range(1, (len(plotList) // 2) + 1):
            x = 0.1
            var = i*x
            shiftList.append(var)
            shiftList.append(var*(-1))

        if len(plotList) % 2 != 0:
            shiftList.append(0)

        shiftList.sort()

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

    def binNumberPlot(self, plotList, caseNameList):

        plt.figure(figsize=(15, 5))

        width = 0.1
        shiftList = []
        values = list(range(len(caseNameList)))
        minimum = float('infinity')
        algorithms = list(plotList.keys())

        for algorithm in plotList:
            minValue = min(plotList[algorithm])
            if minValue < minimum:
                minimum = minValue

        for i in range(1, (len(plotList) // 2) + 1):
            x = 0.1
            var = i*x
            shiftList.append(var)
            shiftList.append(var*(-1))

        if len(plotList) % 2 != 0:
            shiftList.append(0)

        shiftList.sort()

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

    def oldPlot(self, plotList, caseNameList):

        plt.figure(figsize=(20, 5))

        width = 0.05
        shiftList = []
        values = list(range(len(plotList)))
        minimum = float('infinity')
        algorithms = list(plotList.keys())

        tempList = [list(i) for i in zip(*list(plotList.values()))]
        length = len(tempList)

        for i in tempList:
            if min(i) < minimum:
                minimum = min(i)

        for i in range(1, (length // 2) + 1):
            x = 0.05
            var = i*x
            shiftList.append(var)
            shiftList.append(var*(-1))

        if length % 2 != 0:
            shiftList.append(0)

        shiftList.sort()

        for count in range(len(tempList)):
            temp = shiftList[count]
            new_list = [x + temp for x in values]
            plt.bar(new_list, tempList[count], width=width)

        plt.xticks(values, algorithms, rotation=45)
        plt.xlabel('Algorithms')
        plt.ylabel('Number of Bins in Optimal Solution')
        plt.ylim(bottom=minimum - 2)
        plt.legend(caseNameList, loc="lower left", bbox_to_anchor=(1, 0.5))

        plt.show()
