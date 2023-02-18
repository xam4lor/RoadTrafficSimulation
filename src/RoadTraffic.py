from src.Drawer import Drawer
from src.Integrator import Integrator
import numpy as np
import json

class RoadTraffic:
    """
    The RoadTraffic class is responsible for running the simulation.
    """
    def __init__(self):
        # Read configuration file
        fConfig = open("./res/config.json", "r")
        self.config = json.load(fConfig)
        fConfig.close()

        # Create an instance of the Integrator and Drawer class
        self.integrator = Integrator(self)
        self.drawer = Drawer(self)

        # Initialize grid points u (= rho(x,t)))
        self.N = int(self.config["config"]["x_max"] / self.config["config"]["dx"]) # Number of points in the grid
        self.u = np.zeros(self.N) # Grid of points

        # Initial condition (to modify)
        self.u[int(self.N/2)-10:int(self.N/2)+10] = 1 

        # Store the values of u
        self.uValues = np.zeros([int(self.integrator.tMax / self.integrator.dt) + 2, self.N])
        self.uValues[0] = self.u # u[-1] = u0
        self.uValues[1] = self.u # u[0] = u1


    def run(self):
        """
        Run the simulation and draw the plots.
        """
        loopIndex = 1
        print("Running simulation...")
        while (self.integrator.t < self.integrator.tMax):
            # Integrate the system to the next time step
            nextu = self.integrator.step(self.u) 
            self.uValues[loopIndex] = nextu
            self.u = nextu

            # Print the progress
            if int(self.integrator.t * 1000) % int(self.integrator.tMax / 100 * 1000) == 0:
                print("t = " + str(int(self.integrator.t * 10)/10) + " / " + str(self.integrator.tMax) + " s.", end="\r")

            # Next value
            loopIndex += 1

        # Draw the plots
        print("\nDrawing plots...")
        self.drawer.draw()
        print("Done.")
            
