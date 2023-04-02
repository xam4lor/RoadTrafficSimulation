from src.drawer.PlotType import PlotType
import matplotlib.pyplot as plt
from matplotlib import interactive
import numpy as np

class ColorMapPlot(PlotType):
    """
    Plot the roads values at each time step as a color map.

    Parameters
    ----------
    config : Config
        The json configuration.
    roads : array
        The roads to plot.
    """
    def draw(self, config, roads):
        print("Drawing the color map plots...")

        # Plot the density
        plotIndex = 1
        for road in roads:
            xMax = len(road.rho)
            tMax = len(road.rhoValues)

            # Size of dimensions
            xPoints = 200
            tPoints = 200
            x = np.linspace(0, xMax, xPoints)
            t = np.linspace(0, tMax, tPoints)

            # Find corresponding indices
            xIndices = np.arange(0, len(road.rhoValues[0]), len(road.rhoValues[0]) / xPoints)
            tIndices = np.arange(0, len(road.rhoValues), len(road.rhoValues) / tPoints)

            # Create an array for the u values
            u = np.zeros([tPoints, xPoints])
            for i in range(0, tPoints):
                for j in range(0, xPoints):
                    u[i, j] = road.rhoValues[int(tIndices[i])][int(xIndices[j])]

            # Plot the u values as a color map
            plt.figure(plotIndex)
            plt.pcolor(x, t, u, cmap='coolwarm', vmin=0, vmax=1.0)
            plt.colorbar()
            plt.xlabel('Distance from origin $x$ (m)')
            plt.ylabel('Time $t$ (s)')
            plt.title('Density of cars $\\rho(x,t)$ for road ' + road.name)

            # Display the plots
            if plotIndex == 1:
                interactive(True)
            elif plotIndex == len(roads):
                interactive(False)
            plt.show()

            plotIndex = plotIndex + 1
    