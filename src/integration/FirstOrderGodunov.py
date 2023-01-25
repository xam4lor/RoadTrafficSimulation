from src.integration.NumericalScheme import NumericalScheme


class FirstOrderGodunov(NumericalScheme):
    def __init__(self):
        print("FirstOrderGodunov init")

    def integrate(self):
        print("FirstOrderGodunov integrate")

