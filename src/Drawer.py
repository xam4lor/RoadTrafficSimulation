from src.drawer.VideoPlot import VideoPlot
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
    def __init__(self, roadTraffic, plotType):
        # Store the road traffic object
        self.roadTraffic = roadTraffic

        # Make sure the folder for the plots exists
        if not os.path.exists("./out/"):
            os.makedirs("./out/")

        # Select the plot type
        if plotType == "video":
            self.plotTypes = [VideoPlot()]
        elif plotType == "density":
            self.plotTypes = [ColorMapPlot()]


    """
    Draw the plot.
    """
    def draw(self):
        for plotType in self.plotTypes:
            plotType.draw(self.roadTraffic.config, self.roadTraffic.integrator.roads)
