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
        N = 200 # Number of points
        self.u = np.zeros(N) 
        self.u[int(N/2)] = 100

        # All values of ui
        self.uValues = np.zeros([int(self.integrator.tMax / self.integrator.dt), N])
        self.uValues[0] = self.u

    """
    Run the simulation.
    """
    def run(self):
        while (self.integrator.t < self.integrator.tMax):
            # Integrate the system
            nextu = self.integrator.step(self.u)
            index = int(self.integrator.t * self.integrator.dt) 
            self.uValues[index] = nextu
            self.u = nextu

            # Draw the system
            # self.drawer.draw(u)
            
