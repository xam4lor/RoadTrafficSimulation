from src.integration.FirstOrderGodunov import FirstOrderGodunov
import numpy as np 

class Integrator:
    """
    The Integrator class is responsible for integrating the system given a numerical scheme.
    """
    def __init__(self):
        # Select the numerical scheme
        self.numericalScheme = FirstOrderGodunov()

        # Simulation parameters
        self.t = 0
        self.tMax = 1
        self.dt = 0.01
    

    def step(self, u, N):
        """
        Integrate the system to the next time step.

        Parameters
        ----------
        u : array
            The values of u at the previous time step.
        
        N : integer
            Number of points
        """

        # Integrate the system
        nextu = np.zeros(N)
        for i in range(0, N):
            nextu[i] = self.numericalScheme.u(u[i], u[i-1], self.dt)

        # Update the time
        self.t += self.dt

        # Return the values of u at the next time step
        return nextu
