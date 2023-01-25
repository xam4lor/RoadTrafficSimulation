from src.integration.FirstOrderGodunov import FirstOrderGodunov


class Controller:
    def __init__(self):
        self.numericalScheme = FirstOrderGodunov()
        self.numericalScheme.integrate()
        

