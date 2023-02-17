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


    def draw(self):
        """
        Draw the plot.
        """
        self.plotType.draw(self.roadTraffic.uValues)
