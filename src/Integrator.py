from src.integration.FirstOrderGodunov import FirstOrderGodunov
from src.RoadSegment import RoadSegment
import numpy as np 
import json

class Integrator:
    """
    The Integrator class is responsible for integrating the system given a numerical scheme.

    Parameters
    ----------
    roadTraffic : RoadTraffic
        The road traffic object.
    """
    def __init__(self, roadTraffic):
        # Store the road traffic object
        self.roadTraffic = roadTraffic

        # ==== CREATE INTEGRATOR CONFIGURATION ====
        # Select the numerical scheme
        selectedNumericalScheme = roadTraffic.config["selected_scheme_index"] # 1, 2, or 3, corresponding to equation (2.5,6,7)
        self.numericalScheme = FirstOrderGodunov(roadTraffic.config, selectedNumericalScheme)

        # Simulation time parameters
        self.t = 0
        self.tMax = roadTraffic.config["config"]["t_max"]
        self.dt = roadTraffic.config["config"]["dt"]


        # ==== CREATE ROADS ====
        # Open config file for roads
        fRoadsConfig = open('./res/roads.json', 'r')
        roadConfig = json.load(fRoadsConfig)
        fRoadsConfig.close()

        # Create road segments
        self.roads = []
        for road in roadConfig['roads']:
            # Create road segment
            rStart = [
                road['start']['x'] / roadConfig['dimensions']['x'] * roadTraffic.config["config"]["x_max"],
                road['start']['y'] / roadConfig['dimensions']['y'] * roadTraffic.config["config"]["x_max"]
            ]
            rEnd = [
                road['end']['x'] / roadConfig['dimensions']['x'] * roadTraffic.config["config"]["x_max"],
                road['end']['y'] / roadConfig['dimensions']['y'] * roadTraffic.config["config"]["x_max"]
            ]
            rSegment = RoadSegment(roadTraffic, road['name'], rStart, rEnd)

            # Add inflow
            inF = road['inFlow']
            if inF['type'] == 'if':
                r = inF['rate']
                sT = inF['startTime']
                rSegment.addInFlow(lambda t: r if t < sT else 0)
            elif inF['type'] == 'sin':
                a = inF['amplitude']
                f = inF['frequency']
                rSegment.addInFlow(lambda t: a * np.abs(np.sin(f * t)))

            # Add road to list at index
            self.roads.insert(road['id'], rSegment)

        # Connect roads
        for road in roadConfig['roads']:
            for inRoad in road['inRoads']:
                self.roads[road['id']].addInRoads(self.roads[inRoad])
            for outRoad in road['outRoads']:
                self.roads[road['id']].addOutRoads(self.roads[outRoad])


    """
    Step the system forward in time.
    """
    def step(self):
        # Update each road
        for road in self.roads:
            road.step(self.numericalScheme, self.t)

        # Update the time
        self.t += self.dt
