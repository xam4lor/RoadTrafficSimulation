from src.integration.NumericalScheme import NumericalScheme

class FirstOrderGodunov(NumericalScheme):
    def u(self, ui, uLefti, dt):
        vm = 10
        rhom = 10
        dx = 0.01
        return ui - vm * (1.0 - 2.0 * ui / rhom) * dt / dx * (ui - uLefti)
    
