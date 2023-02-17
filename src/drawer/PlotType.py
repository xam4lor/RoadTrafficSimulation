class PlotType:
    """
    Generic class for all plot types.
    """
    def draw(self, uValues):
        """
        Draw the system.

        Parameters
        ----------
        uValues : array
            The values of u at each time step.
        """
        raise NotImplementedError("Draw method not implemented")
