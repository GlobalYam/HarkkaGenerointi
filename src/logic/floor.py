import numpy as np


class Floor:
    """Luokka joka kuvaa yhtä kerrosta"""

    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width

        # Alustaa tyhjän numpy arrayn nollilla halutussa muodossa
        self.grid = np.zeros((height, width))

        # reunusta ykkösllä
        self.grid[0, :] = 1  # ylä
        self.grid[-1, :] = 1  # ala
        self.grid[:, 0] = 1  # vasen
        self.grid[:, -1] = 1  # oieka

    def __str__(self):
        return "".join([f"{row}\n" for row in self.grid])
