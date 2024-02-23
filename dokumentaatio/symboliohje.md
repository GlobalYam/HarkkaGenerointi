# Symbolit


Ohjelma hyödyntää pääosaksi numpy.array teitorakennetta jossa luvut kuvaavat eri Tile paloja.
Jokaisella Tile-palalla on omat naapuruussäännöt jotka sallivat tai kieltävät palaa olemasta toisen vieressä.

Tile palaset voivat configuroida miten haluaa, eli esim. wavefuction collapse algoritmi on suunniteltu olemaan Tile agnostinen.
Eli funktion tulisi ottaa syötteeksi pari naapuruussääntöjä ja osittain täytetty numpyarray, jonka wavefuntioncollapse täyttää naapuruussääntöjä noudattaen.

Oletusasetuksilla numerot kuitenkin kuvaavat seuraavia stuktuureja videopelityylisessä tasossa:

0: Tyhjä tile. 
1: Kallio.     4,4,0,0
2: Seinä.      4,3,4,2
3. Lattia.     0,3,4,2
4. Käytävä.    0,2,1,2

Tilejä seuraavat numerot kertovat kuinka monta mitäkin naapuria kyseisellä laatalla saa olla.
Esim Lattia-laatan vieressä saa olla 0 kallio palaa, 3 seinäpalaa, 4 lattiapalaa, ja 2 käytäväpalaa.
Tämä tarkoittaa että lattialaatat voivat helposti kattaa laajan alueen, 
kun taas käytäväpalat luovat tunnelimaisia raktenteita huoneiden välille. 