import matplotlib.pyplot as plt
from helpers import getCaseName

class Plotter():

    def oraclePlot(self, plotList, caseNameList):

        # plotlist = {key: [value1, value2, value3], key2: [value1, value2, value3]}

        fig, ax = plt.subplots() 

        for algorithm, output in plotList.items():
            ax.plot(caseNameList, output, label = algorithm)

        ax.set_title('Algorithm Output of Number of Bins for Each Dataset Case')
        ax.set_xlabel('Dataset Cases')
        ax.set_ylabel('Number of Bins in Optimal Solution')
        plt.xticks(rotation = 50)

        pos = ax.get_position()
        ax.set_position([pos.x0, pos.y0, pos.width * 0.9, pos.height])
        ax.legend(loc='center right', bbox_to_anchor=(1.5, 1))

        plt.show()

        return

    def oraclePlot2(self, plotList, caseNameList):

        length = 0
        width = 0.2
        shiftList = []
        values = list(range(len(plotList)))

        tempList = [list(i) for i in zip(*list(plotList.values()))]
        length = len(tempList)
        
        for i in range(1, (length // 2) + 1):
            x = width/2
            var = i*x
            shiftList.append(var)
            shiftList.append(var*(-1))

        if length % 2 != 0:
            shiftList.append(0)

        shiftList.sort()

        for count, key in enumerate(tempList):
            temp = shiftList[count]
            new_list = [x + temp for x in values]
            plt.bar(new_list, tempList[count], width=width)

        algorithms = list(plotList.keys())

        plt.xticks(values, algorithms, rotation = 45)
        plt.xlabel('Algorithms')
        plt.ylabel('Number of Bins in Optimal Solution')
        plt.legend(caseNameList, loc="lower left", bbox_to_anchor=(1, 0.5))

        plt.show()