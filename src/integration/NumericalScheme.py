class NumericalScheme:
    """
    Generic class to describe a numerical scheme for solving a system of equations.
    """
    def u1(self, ui, uLefti, dt):
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
        raise NotImplementedError("Error: u1() not implemented")


    def u2(self, ui, uLefti, dt):
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
        raise NotImplementedError("Error: u2() not implemented")


    def u3(self, ui, uLefti, dt):
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
        raise NotImplementedError("Error: u3() not implemented")
