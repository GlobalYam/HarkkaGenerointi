# Symbolit


Ohjelma hyödyntää pääosaksi numpy.array teitorakennetta jossa luvut kuvaavat eri Tile paloja.
Jokaisella Tile-palalla on omat naapuruussäännöt jotka sallivat tai kieltävät palaa olemasta toisen vieressä.

Tile palaset voivat configuroida miten haluaa, eli esim. wavefuction collapse algoritmi on suunniteltu olemaan Tile agnostinen.
Eli funktion tulisi ottaa syötteeksi pari naapuruussääntöjä ja osittain täytetty numpyarray, jonka wavefuntioncollapse täyttää naapuruussääntöjä noudattaen.

Oletusasetuksilla numerot kuitenkin kuvaavat seuraavia stuktuureja videopelityylisessä tasossa:

0: Tyhjä tile.
1: Seinä.
2: Lattia.
3. Käytävä.
4. Ovi.
5. Kallio.