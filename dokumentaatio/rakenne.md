# Rakennedokumentti

Ohjelman rakenne on jaettu kahteen osaan:
1. Ohjelman Käyttämät Algoritmit
2. Käyttäjän näkymä

Pyrin suorittamaan algoritmit mahdollisen selkeästi ja modulaarisesti yhden tehtävän periaatteella.
Käyttäjän näkymä koostuu UIn lisäksi algoritmeja yhdistävästä koodista, 
jonka vastuu on käsitellä algoritmien tulokset ja syötteet oikeaan mmuotoon.

Käyttäjän näkymä on toteutettu pygamella, joka vastaa syötteen vastaanotosta ja näytölle piirtämisestä.

Tason generointi tulee koostumaan metodeista jotka hyödyntävät soluautomaatiota ja wavefunctioncollapse algoritmia.
Käyttämäni wavefunctioncollapse pyrkii saavuttamaan samankaltaisia tuloksia, kuin käyttäjän [mxgmn wavefunctioncollapse algoritmi](https://github.com/mxgmn/WaveFunctionCollapse)*
Kyseinen toteutus käsittelee kuvaa NxN (tyypillisesi 3x3) kokoisissa patterneissa, tämä metodi on huomattavasti monimutkaisempi kuin klassinen wavefuctioncollapse, 
sillä kyseinen toteutus säilyttää eri NxN patternien suhteellisen määrän inputin ja outputin välillä.
Tämän tuloksena output kuva muistuttaa input kuvaa lokaalisti sekä makrotasolla.

Ohjelmani rakenne tukee myös osittain täytetyn output kuvan syöttämistä input kuvan kanssa, jolloin wavefunctioncollapse suoritetaan osittain täytetylle kuvalle.

Esimerkki Kevin Chapelierin selainmallin toiminnasta:

![lähedekuva](https://github.com/GlobalYam/HarkkaGenerointi\dokumentaatio\dokumentaatiokuvat\bricks_original.png)

N=2 muistuttaa tyypillisempää wavefunctioncollapse algoritmia:

[N=2](dokumentaatio\dokumentaatiokuvat\bricks_2x2.png)


N=3 huomattavasti tarkempi kuva, ja huomattavasti haastavmpi implementoida:

[N=3](dokumentaatio\dokumentaatiokuvat\bricks_3x3.png) 

*(Copyright (c) 2014 Kevin Chapelier under the MIT liscence)[https://github.com/kchapelier/wavefunctioncollapse?tab=MIT-1-ov-file#readme]