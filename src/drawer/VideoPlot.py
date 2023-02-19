from src.drawer.PlotType import PlotType
from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np

class VideoPlot(PlotType):
    """
    Plot the u values as a video.
    """
    def draw(self, config, uValues):
        print("Drawing the video plot...")
        # Size of dimensions
        xPoints = 200
        tPoints = 100
        x = np.linspace(0, config["config"]["x_max"], xPoints)
        dt = int(tPoints / config["config"]["t_max"])

        # Find corresponding indices
        xIndices = np.arange(0, len(uValues[0]), len(uValues[0]) / xPoints)
        tIndices = np.arange(2, len(uValues), len(uValues) / tPoints)

        # Initialize the plot
        fig = plt.figure()
        line, = plt.plot([], [])
        plt.xlim(0, config["config"]["x_max"])
        plt.ylim(0, 1)
        plt.xlabel('Distance from origin $x$ (m)')
        plt.ylabel('Density of cars $\\rho(x,t)$ (m$^{-1}$)')
        plt.title('Density of cars $\\rho(x,t)$ at $t = 0$ s')

        # Make the animation
        def animate(i):
            # Update title
            t = round(tIndices[i] * config["config"]["dt"], 1)
            plt.title('Density of cars $\\rho(x,t)$ at $t = ' + str(t) + '$ s')

            # Progress bar
            if i == tPoints - 1:
                print("t = " + str(config["config"]["t_max"]) + " / " + str(config["config"]["t_max"]) + " s.")
            else:
                print("t = " + str(round(tIndices[i] * config["config"]["dt"], 1)) + " / " + str(config["config"]["t_max"]) + " s.", end="\r")

            # Update line
            u = np.zeros(xPoints)
            for j in range(0, xPoints):
                u[j] = uValues[int(tIndices[i]), int(xIndices[j])]
            line.set_data(x, u)
            return line,

        # Write the animation to a file
        ani = animation.FuncAnimation(fig, animate, frames=tPoints, interval=dt, blit=True, repeat=False)
        writer = animation.writers['ffmpeg'](fps=dt)
        ani.save('./output/densityvideo.mp4', writer=writer, dpi=100)
        
