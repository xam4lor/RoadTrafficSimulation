class PlotType:
    """
    Generic class for all plot types.
    """
    def draw(self, config, uValues):
        """
        Draw the system.

        Parameters
        ----------
        config : dict
            The configuration dictionary.
        uValues : array
            The values of u at each time step.
        """
        raise NotImplementedError("Draw method not implemented")
