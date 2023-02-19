from src.drawer.ColorMapPlot import ColorMapPlot
import os

class Drawer:
    """
    This class is responsible for drawing the plot.

    Parameters
    ----------
    roadTraffic : RoadTraffic
        The road traffic object.
    """
    def __init__(self, roadTraffic):
        # Store the road traffic object
        self.roadTraffic = roadTraffic

        # Make sure the folder for the plots exists
        if not os.path.exists("./output/"):
            os.makedirs("./output/")

        # Select the plot type
        self.plotType = ColorMapPlot()


    def draw(self):
        """
        Draw the plot.
        """
        self.plotType.draw(self.roadTraffic.config, self.roadTraffic.uValues)
