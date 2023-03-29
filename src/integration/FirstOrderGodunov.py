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
        self.vm = config["schemes"]["first_order_godunov"]["vm"]
        self.rhom = config["schemes"]["first_order_godunov"]["rhom"]
        self.a = config["schemes"]["first_order_godunov"]["a"]

        self.dx = config["config"]["dx"]
        self.dt = config["config"]["dt"]

        # Select the numerical scheme
        if selectNumericalScheme == 1:
            self.selectNumericalScheme = self.u1
        elif selectNumericalScheme == 2:
            self.selectNumericalScheme = self.u2
        elif selectNumericalScheme == 3:
            self.selectNumericalScheme = self.u3

    def u(self, ui, uLefti, x, t):
        ans = self.selectNumericalScheme(ui, uLefti, x, t)
        if ans < 0:
            return 0
        if ans > 1:
            return 1
        return ans


    ### Numerical schemes ###
    def u1(self, ui, uLefti, x, t):
        rho0 = 2 
        v = self.vm
        return ui - v * (1.0 - 2.0 * rho0 / self.rhom) * self.dt / self.dx * (ui - uLefti)
    
    def u2(self, ui, uLefti, x, t):
        rho0 = 2 
        v = self.vm
        return ui - v * (1.0 - rho0 / self.rhom) * self.dt / self.dx * (ui - uLefti) * np.exp(- rho0 / self.rhom)
    
    def u3(self, ui, uLefti, x, t):
        rho0 = 2 
        v = self.vm
        return ui - v * (1.0 - (rho0 / self.rhom)**self.a) * self.dt / self.dx * (ui - uLefti) * np.exp(-(1.0 / self.a) * (rho0 / self.rhom)**self.a)
