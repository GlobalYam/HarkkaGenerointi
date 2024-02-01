import numpy


class SimpleWavefuntioncollapse:
    """Luokka joka toteuttaa annetulle numpyarraylle yksinkertaisen wavefunctioncollapse algoritmin"""

    def __init__(self, level, adjacency_rules) -> None:
        self.level = level
        self.adjacency_rules = adjacency_rules
