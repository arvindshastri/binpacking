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
