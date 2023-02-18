from src.integration.NumericalScheme import NumericalScheme
import numpy as np

class FirstOrderGodunov(NumericalScheme):
    """
    First order Godunov scheme.

    Parameters
    ----------
    config : dict
        The configuration dictionary.
    selectNumericalScheme : int
        The numerical scheme index to use.
    """
    def __init__(self, config, selectNumericalScheme):
        # Parameters
        self.dx = config["config"]["dx"]
        self.vm = config["schemes"]["first_order_godunov"]["vm"]
        self.rhom = config["schemes"]["first_order_godunov"]["rhom"]
        self.a = config["schemes"]["first_order_godunov"]["a"]

        # Select the numerical scheme
        if selectNumericalScheme == 1:
            self.selectNumericalScheme = self.u1
        elif selectNumericalScheme == 2:
            self.selectNumericalScheme = self.u2
        elif selectNumericalScheme == 3:
            self.selectNumericalScheme = self.u3

    def u(self, ui, uLefti, dt):
        return self.selectNumericalScheme(ui, uLefti, dt)


    ### Numerical schemes ###
    def u1(self, ui, uLefti, dt):
        return ui - self.vm * (1.0 - 2.0 * ui / self.rhom) * dt / self.dx * (ui - uLefti)
    
    def u2(self, ui, uLefti, dt):
        return ui - self.vm * (1.0 - ui / self.rhom) * dt / self.dx * (ui - uLefti) * np.exp(-ui / self.rhom)
    
    def u3(self, ui, uLefti, dt):
        return ui - self.vm * (1.0 - (ui / self.rhom)**self.a) * dt / self.dx * (ui - uLefti) * np.exp(-(1.0 / self.a) * (ui / self.rhom)**self.a)
