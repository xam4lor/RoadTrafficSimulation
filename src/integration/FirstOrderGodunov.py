from src.integration.NumericalScheme import NumericalScheme

class FirstOrderGodunov(NumericalScheme):
    def u(self, i, n, uPrev):
        # Return the value of u at position i and time n using the previous time step
        return 0
