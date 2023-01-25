class NumericalScheme:
    """
    Describes a numerical scheme for solving a system of equations.
    """
    def u(self, i, n, uPrev):
        """
        Integrate the system to the next time step.

        Parameters
        ----------
        i : int
            The index of the cell.
        n : int 
            The index of the time step.
        uPrev : array
            The values of u at the previous time step.
        """
        print("Error: u() not implemented")
