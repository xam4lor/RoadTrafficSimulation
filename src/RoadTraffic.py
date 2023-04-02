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


    """
    Run the simulation.
    """
    def run(self):
        print("Running simulation...")
        while (self.integrator.t < self.integrator.tMax):
            # Integrate the system to the next time step
            self.integrator.step()

            # Print the progress
            if int(self.integrator.t * 1000) % int(self.integrator.tMax / 100 * 50) == 0:
                print("Simulation percentage = " + str(int(self.integrator.t / self.integrator.tMax * 100)) + "%.", end="\r")

        # Draw the plots
        print("\nDrawing plots and animations...")
        self.drawer.draw()
        print("Animation saved in the './out' folder.")
            
