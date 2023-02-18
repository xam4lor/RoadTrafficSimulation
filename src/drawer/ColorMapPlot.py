from src.drawer.PlotType import PlotType
import matplotlib.pyplot as plt
import numpy as np

class ColorMapPlot(PlotType):
    """
    Plot the u values at each time step as a color map.
    """
    def draw(self, config, uValues):
        # Size of dimensions
        xPoints = 200
        tPoints = 200
        x = np.linspace(0, config["config"]["x_max"], xPoints)
        t = np.linspace(0, config["config"]["t_max"], tPoints)

        # Find corresponding indices
        xIndices = np.zeros(xPoints)
        tIndices = np.zeros(tPoints)
        for i in range(0, xPoints):
            xIndices[i] = int(i * len(uValues[0]) / xPoints)
        for i in range(0, tPoints):
            tIndices[i] = int(i * len(uValues) / tPoints + 2)

        # Create an array for the u values
        u = np.zeros([tPoints, xPoints])
        for i in range(0, tPoints):
            for j in range(0, xPoints):
                u[i, j] = uValues[int(tIndices[i]), int(xIndices[j])]

        # Plot the u values as a color map
        plt.figure()
        plt.pcolor(x, t, u, cmap='coolwarm')
        plt.colorbar()
        plt.xlabel('Distance from origin $x$ (m)')
        plt.ylabel('Time $t$ (s)')
        plt.title('Density of cars $\\rho(x,t)$')

        # Save the plot
        plt.savefig("./output/colormapplot.png")
        plt.show()
    