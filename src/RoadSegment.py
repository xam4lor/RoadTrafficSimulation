import numpy as np

class RoadSegment:
    """
    The RoadSegment class represents a road segment.

    Parameters
    ----------
    roadTraffic : RoadTraffic
        The road traffic object.
    name : str
        The name of the road.
    start : list
        The start position of the road.
    end : list
        The end position of the road.
    """
    def __init__(self, roadTraffic, name, start, end):
        self.name = name
        self.inRoads = []  # Incoming roads
        self.outRoads = []  # Outgoing roads
        self.inFlow = None  # Inflow function

        self.dx = roadTraffic.config["config"]["dx"]
        self.dt = roadTraffic.config["config"]["dt"]

        self.startPos = start
        self.endPos = end
        self.L = np.sqrt(np.power(start[0] - end[0], 2) + np.power(start[1] - end[1], 2))

        self.lastRho = np.zeros(int(self.L / self.dx))  # u_i^n-1
        self.rho = np.zeros(int(self.L / self.dx))  # u_i^n
        self.rhoValues = [] # List of all rho values over time


    """
    The step function updates the road segment.
    
    Parameters
    ----------
    scheme : Scheme
        The numerical scheme method to call.
    t : float
        The current time.
    """
    def step(self, scheme, t):
        # Clear new rho values
        self.rho = np.zeros(len(self.rho))

        # Update all cells apart from the first and last
        for i in range(0, len(self.rho)):
            lastRho = self.lastRho[i-1]
            if i == 0:
                lastRho = 0 # If there are no incoming roads, set the lastRho to 0

                # Add the inflow
                if self.inFlow is not None:
                    lastRho += self.inFlow(t)

                # Compute the number that the previous roads is sending to
                previousRoadsOutCount = []
                for inRoadIndex in range(len(self.inRoads)):
                    previousRoadsOutCount.append(len(self.inRoads[inRoadIndex].outRoads))

                # Connect to the last cells of the previous roads
                for inRoadIndex in range(len(self.inRoads)):
                    inRoad = self.inRoads[inRoadIndex]
                    lastRho += inRoad.lastRho[inRoad.lastRho.size - 1] / previousRoadsOutCount[inRoadIndex]

            # Update the cell
            self.rho[i] = scheme.u(self.lastRho[i], lastRho, i * self.dx, t)

        # Update last values
        self.lastRho = self.rho

        # Save rho values
        self.rhoValues.append(self.rho)


    """
    The addInFlow function adds an inflow function to the road segment.

    Parameters
    ----------
    inFlow : function
        The inflow function that takes a time parameter.
    """
    def addInFlow(self, inFlow):
        self.inFlow = inFlow

    """
    The addInRoads function add incoming roads to the road segment.

    Parameters
    ----------
    *roads : RoadSegment
        The incoming roads.
    """
    def addInRoads(self, *roads):
        for road in roads:
            self.inRoads.append(road)


    """
    The addOutRoads function add outgoing roads to the road segment.

    Parameters
    ----------
    *roads : RoadSegment
        The outgoing roads.
    """
    def addOutRoads(self, *roads):
        for road in roads:
            self.outRoads.append(road)
    