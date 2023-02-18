from src.integration.FirstOrderGodunov import FirstOrderGodunov
import numpy as np 

class Integrator:
    """
    The Integrator class is responsible for integrating the system given a numerical scheme.
    """
    def __init__(self, roadTraffic):
        # Store the road traffic object
        self.roadTraffic = roadTraffic

        # Select the numerical scheme
        selectedNumericalScheme = roadTraffic.config["selected_scheme_index"] # 1, 2, or 3, corresponding to equation (2.5,6,7)
        self.numericalScheme = FirstOrderGodunov(roadTraffic.config, selectedNumericalScheme)

        # Simulation time parameters
        self.t = 0
        self.tMax = roadTraffic.config["config"]["t_max"]
        self.dt = roadTraffic.config["config"]["dt"]
    

    def step(self, u):
        """
        Integrate the system to the next time step.

        Parameters
        ----------
        u : array
            The values of u at the previous time step.

        Returns
        -------
        nextu : array
            The values of u at the next time step.
        """
        # Compute the values of u at the next time step
        nextu = np.zeros(self.roadTraffic.N)
        for i in range(0, self.roadTraffic.N):
            nextu[i] = self.numericalScheme.u(u[i], u[i-1], self.dt)

        # Update the time
        self.t += self.dt

        # Return the values of u at the next time step
        return nextu
