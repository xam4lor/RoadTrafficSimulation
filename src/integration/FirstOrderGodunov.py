from src.integration.NumericalScheme import NumericalScheme
import numpy as np

class FirstOrderGodunov(NumericalScheme):
    def u1(self, ui, uLefti, dt):
        vm = 10
        rhom = 10
        dx = 0.01
        return ui - vm * (1.0 - 2.0 * ui / rhom) * dt / dx * (ui - uLefti)
    

    def u2(self, ui, uLefti, dt):
        vm = 10
        rhom = 10
        dx = 0.01
        return ui - vm * (1.0 - ui / rhom) * dt / dx * (ui - uLefti) * np.exp(- ui / rhom)
    
    
    def u3(self, ui, uLefti, dt):
        vm = 10
        rhom = 10
        dx = 0.01
        a = 4
        return ui - vm * (1.0 - (ui / rhom)**a) * dt / dx * (ui - uLefti) * np.exp(- (1 / a) * (ui / rhom)**a)
