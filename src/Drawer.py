from src.drawer.ColorMapPlot import ColorMapPlot

class Drawer:
    """
    This class is responsible for drawing the plot.
    """
    def __init__(self, roadTraffic):
        # Store the road traffic object
        self.roadTraffic = roadTraffic

        # Select the plot type
        self.plotType = ColorMapPlot()


    def draw(self, uValues):
        """
        Draw the plot.
        
        Parameters
        ----------
        uValues : array
            All values of u.
        """
        self.plotType.draw(uValues)
