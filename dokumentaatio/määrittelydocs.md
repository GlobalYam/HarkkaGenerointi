# Määrittelydokumentti

## Aihevalinta
Valitsemani aihe on Luolageneroitnisysteemi joka hyödyntää WavefuntionCollapse algoritmia huoneiden yksityiskohtia varten.

## Toteutus
Totutan projektin pythonilla. 
Valitsin pythonin sillä minulla ei ole tarpeeksi kokemusta muissa kielissä toteutusta varten.
En myöskään usko että pystyn vertaisarvioimaan muita kuin python projekteja

## Kuvaus ja vaatimukset
Ohjelman tulisi toimia saamalla syötteenä kerroksen koko, ja huonemalleja.
Ohjelma hyödyntää generointialgoritmia huonepohjien generointiin ja yhdistämiseen,
Ohjelma sitten täyttää yksittäiset huoneet yksityiskohdilla hyödyntäen wavefuctioncollapse algoritmia.
Wavefunctioncollapse algoritmi hyödyntää annettua esimerkkikuvaa vierekkäisyyssääntöjen selvittämistä varten.

## Algoritmit ja tietorakenteet
Kerrokset käsitellään ja tallennetaan NumPy arrayna.
Kerroksien luomista varten tulen soveltamaan laajennettua wavefunctioncollapse algoritmia, 
jota tulen myös mahdollisesti täydentämään muilla tasonluontiin soveltuvilla algoritmeilla.

## Dokumentaatio
Dokumentaatio tehty markdownilla ja koodikommentit docstringillä


## Wavefunctioncollapse
Aloitan implementoimalla yksinkertaisen wavefuctioncollapse algoritmin, jota tulen laajentamaan.

Toteutuksen ytimessä tulee olemaan laajennettu versio wavefunctioncollapse algoritmista.

Tason generointi tulee koostumaan metodeista jotka hyödyntävät soluautomaatiota ja wavefunctioncollapse algoritmia.
Käyttämäni wavefunctioncollapse pyrkii saavuttamaan samankaltaisia tuloksia, kuin käyttäjän [mxgmn wavefunctioncollapse algoritmi](https://github.com/mxgmn/WaveFunctionCollapse)*
Kyseinen toteutus käsittelee kuvaa NxN (tyypillisesi 3x3) kokoisissa patterneissa, tämä metodi on huomattavasti monimutkaisempi kuin klassinen wavefuctioncollapse, 
sillä kyseinen toteutus säilyttää eri NxN patternien suhteellisen määrän inputin ja outputin välillä.
Tämän tuloksena output kuva muistuttaa input kuvaa lokaalisti sekä makrotasolla.

Päämääräni on toteuttaa ohjelmani rakenne siten että se tukee osittain täytetyn output kuvan syöttämistä input kuvan kanssa, jolloin wavefunctioncollapse suoritetaan osittain täytetylle kuvalle.

Esimerkki Kevin Chapelierin selainmallin toiminnasta:
|                                                          lähdekuva                                                          | n=2                                                                                                             | n=3                                                                                                             |
| :-------------------------------------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------- |
| ![lähedekuva](https://github.com/GlobalYam/HarkkaGenerointi/blob/main/dokumentaatio/dokumentaatiokuvat/bricks_original.png) | ![N=2](https://github.com/GlobalYam/HarkkaGenerointi/blob/main/dokumentaatio/dokumentaatiokuvat/bricks_2x2.png) | ![N=3](https://github.com/GlobalYam/HarkkaGenerointi/blob/main/dokumentaatio/dokumentaatiokuvat/bricks_3x3.png) |

N=2 muistuttaa tyypillisempää wavefunctioncollapse algoritmia, kun taas N=3 tuottaa huomattavasti vaikuttavamman tuloksen.

*(Copyright (c) 2014 Kevin Chapelier under the MIT liscence)[https://github.com/kchapelier/wavefunctioncollapse?tab=MIT-1-ov-file#readme]
