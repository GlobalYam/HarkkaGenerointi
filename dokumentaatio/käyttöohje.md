# Käyttöohje

Latausta varten kloonaa repositorio omalle laittellesi ja suorita komennot

~~~
poetry install
~~~
~~~
poetry shell
~~~
~~~
python src/index.py
~~~

## Komennot
Ohjelmä hyödyntää seuraavia komentoja:

## E:
E-näppäin päivittää näkymään entropian, jossa 0 tarkoittaa asetettua solua, ja 1 suuremmat numerot kuvaavat saatavilla olevia vaihtoehtoja

## U:
U-näppäin päivittää näkymän normaaliksi, tällä voi palauttaa näkymän normaaliksi E-näppäimen painamisen jälkeen

## C:
C-näppäin toteuttaa askeleen WFC algoritmia ja päivittää näkymän

## A:
A-näppäin automaattisesti totetuttaa WFC askelia kunnes ruudukon matalin entropia on 0

## R:
R-näppäin resetoi ruudukon

debug komentoja:
## W:
W-näppäin päivittää entropian manuaalisesti. Käytetään jos kohdataan jumittuminen, sekä kehityksen kannalta hyödyllinen
