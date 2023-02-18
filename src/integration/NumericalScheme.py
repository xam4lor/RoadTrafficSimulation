class NumericalScheme:
    """
    Generic class to describe a numerical scheme for solving a system of equations.
    """
    def u(self, ui, uLefti, x, t):
        """
        Integrate the system to the next time step.

        Parameters
        ----------
        ui : float
            The values of ui at the previous time step.
        uLefti : float
            The values of uLefti at the previous time step.
        x : float   
            The x coordinate.
        t : float
            The t coordinate.
        """
        raise NotImplementedError("Error: u() not implemented")
