from src.integration.FirstOrderGodunov import FirstOrderGodunov

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
    

    def step(self, u):
        """
        Integrate the system to the next time step.

        Parameters
        ----------
        u : array
            The values of u at the previous time step.
        """

        # Integrate the system
        # Calculate the values of u at the next time step using self.numericalScheme.u()
        # Todo ........

        # Update the time
        self.t += self.dt

        # Return the values of u at the next time step
        return u
