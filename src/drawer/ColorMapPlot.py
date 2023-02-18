from src.drawer.PlotType import PlotType
import matplotlib.pyplot as plt
import numpy as np

class ColorMapPlot(PlotType):
    """
    Plot the u values at each time step as a color map.
    """
    def draw(self, config, uValues):
        # Size of dimensions
        Nt = int(len(uValues)/10)
        Nx = len(uValues[0])
        x = np.linspace(0, 1, Nx)
        t = np.linspace(0, config["config"]["t_max"], Nt)

        # Create an array for the u values
        u = np.zeros((Nt, Nx))
        for i in range(0, Nt):
            for j in range(0, Nx):
                u[i, j] = uValues[i][j]

        # Plot the u values as a color map
        plt.figure()
        plt.pcolor(x, t, u, cmap='coolwarm')
        plt.colorbar()
        plt.xlabel('x')
        plt.ylabel('t')
        plt.title('Density of cars $\\rho(x,t)$')

        # Save the plot
        plt.savefig("./output/colormapplot.png")
        plt.show()
    