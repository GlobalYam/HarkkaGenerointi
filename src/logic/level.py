import numpy as np


class Level:
    """Luokka joka kuvaa yhtä kerrosta"""

    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width

        # Alustaa tyhjän numpy arrayn nollilla halutussa muodossa
        self.grid = np.zeros((height, width))

        # reunusta xkkösllä
        self.grid[0, :] = 1  # ylä
        self.grid[-1, :] = 1  # ala
        self.grid[:, 0] = 1  # vasen
        self.grid[:, -1] = 1  # oieka

    def add_room(self, coordinates, height, width):
        """Funktio joka asettaa huoneen annettuihin kordinaatteihin jos se on sallittua"""
        x, y = coordinates

        # Tarkista sallitaanko huoneen asettaminen
        if (
            0 < y < self.height - height
            and 0 < x < self.width - width
            and np.all(self.grid[y : y + height, x : x + width] == 0)
        ):
            # Rakenna huone
            self.grid[y, x : x + width] = 1  # Yläseinä
            self.grid[y + height - 1, x : x + width] = 1  # Pohjaseinä
            self.grid[y : y + height, x] = 1  # Vasenseinä
            self.grid[y : y + height, x + width - 1] = 1  # Oikeaseinä

            # Täytä huone lattialla
            self.grid[y + 1 : y + height - 1, x + 1 : x + width - 1] = 2

            print("Huone rakennettu")
            return True
        else:
            print("Huonetta ei voi rakentaa")
            return False

    def add_floor(self, coordinates, height, width):
        """Funktio joka asettaa lattiaa annettuihin kordinaatteihin"""
        x, y = coordinates

        # Tarkista sallitaanko huoneen asettaminen
        if (
            0 < y < self.height - height
            and 0 < x < self.width - width
            and np.all(self.grid[y : y + height, x : x + width] != 1)
        ):
            # Täytä lattialla
            self.grid[y : y + height, x : x + width] = 2

            print("Huone rakennettu")
            return True
        else:
            print("Huonetta ei voi rakentaa")
            return False

    def __str__(self):
        return "".join([f"{row}\n" for row in self.grid])
