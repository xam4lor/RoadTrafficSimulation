class PlotType:
    """
    Generic class for all plot types.

    Parameters
    ----------
    config : Config
        The json configuration.
    roads : array
        The roads to plot.
    """
    def draw(self, config, roads):
        """
        Draw the system.

        Parameters
        ----------
        config : dict
            The configuration dictionary.
        """
        raise NotImplementedError("Draw method not implemented")
