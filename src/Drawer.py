from src.drawer.ColorMapPlot import ColorMapPlot

class Drawer:
    """
    This class is responsible for drawing the plot.
    """
    def __init__(self):
        self.plotType = ColorMapPlot()

    def draw(self, uValues):
        """
        Draw the plot.
        
        Parameters
        ----------
        uValues : array
            All values of u.
        """
        indexLook = 150
        self.plotType.draw(uValues[indexLook])
