from src.Drawer import Drawer
from src.Integrator import Integrator
import numpy as np

class RoadTraffic:
    """
    The RoadTraffic class is responsible for running the simulation.
    """
    def __init__(self):
        # Create an instance of the Integrator class
        self.integrator = Integrator()

        # Create an instance of the Drawer class
        self.drawer = Drawer()

        # Initialize u
        self.N = 200 # Number of points
        self.u = np.zeros(self.N) 
        self.u[int(self.N/2)] = 100

        # All values of ui
        self.uValues = np.zeros([int(self.integrator.tMax / self.integrator.dt) + 2, self.N])
        self.uValues[0] = self.u
        self.uValues[1] = self.u

    """
    Run the simulation.
    """
    def run(self):
        index = 1
        while (self.integrator.t < self.integrator.tMax):
            # Integrate the system
            nextu = self.integrator.step(self.u, self.N) 
            self.uValues[index] = nextu
            self.u = nextu

            # Next value
            index += 1

        # Draw the plot
        self.drawer.draw(self.uValues)
            
