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
Kerroksen luomisessa hyödynnetään eri algoritmeja huonepohjien luomiseen, ja niiden yhdistämiseen käytävillä.
Lopuksi wavefunctioncollapse algoritmia käytetään huonepohjien täyttämiseen.

## Dokumentaatio
Dokumentaatio tehty markdownilla ja koodikommentit docstringillä