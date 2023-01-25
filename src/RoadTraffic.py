from src.Integrator import Integrator

class RoadTraffic:
    """
    The RoadTraffic class is responsible for running the simulation.
    """
    def __init__(self):
        # Create an instance of the Integrator class
        self.integrator = Integrator()

    """
    Run the simulation.
    """
    def run(self):
        while (self.integrator.t < self.integrator.tMax):
            # Integrate the system
            #self.integrator.step(u)

            # Draw the system
            # ...
