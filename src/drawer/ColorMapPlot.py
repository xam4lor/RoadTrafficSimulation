from src.drawer.PlotType import PlotType
import matplotlib.pyplot as plt
import numpy as np

class ColorMapPlot(PlotType):
    def draw(self, u):
        index = 10

        # Scatter plot
        plt.scatter(np.linspace(0, 1, len(u[index])), u[index])
        plt.show()

    