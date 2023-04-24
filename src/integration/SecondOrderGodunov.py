from src.integration.NumericalScheme import NumericalScheme
import numpy as np

## Il manque uRight et Alpha à rajouter dans la classe
class SecondOrderGodunov(NumericalScheme):
    """
    Second order Godunov scheme.

    Parameters
    ----------
    config : dict
        The configuration dictionary.
    """
    def __init__(self, config, selectNumericalScheme):
        # Parameters
        self.vm = config["schemes"]["second_order_godunov"]["vm"]
        self.rhom = config["schemes"]["second_order_godunov"]["rhom"]
        self.a = config["schemes"]["second_order_godunov"]["a"]
        self.alpha = config["schemes"]["second_order_godunov"]["alpha"]

        self.dx = config["config"]["dx"]
        self.dt = config["config"]["dt"]

    ### Numerical schemes ###
    def u(self, ui, uLefti, uRighti, x, t):
        v = self.vm
        return ui - v * (1.0 - 2.0 * ui / self.rhom) * self.dt / self.dx * (ui - uLefti) + self.alpha * self.dt / self.dx**2 * (uRighti - 2*ui + uLefti)
    