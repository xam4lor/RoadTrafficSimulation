class NumericalScheme:
    """
    Describes a numerical scheme for solving a system of equations.
    """
    def u(self, ui, uLefti, dt):
        """
        Integrate the system to the next time step.

        Parameters
        ----------
        ui : float
            The values of ui at the previous time step.
        uLefti : float
            The values of uLefti at the previous time step.
        dt : float
            Timestep.
        """
        print("Error: u() not implemented")
