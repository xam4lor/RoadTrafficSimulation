from src.integration.NumericalScheme import NumericalScheme

class FirstOrderGodunov(NumericalScheme):
    def u(self, ui, uLefti, dt):
        vm = 1
        rhom = 1
        dx = 1
        return ui - vm * (1 - 2 * ui / rhom) * dt / dx * (ui - uLefti)
    
