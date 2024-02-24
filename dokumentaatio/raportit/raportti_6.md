# viikkoraportti 6

Aloitin vertaisarvioinnin maanantaina perehtymällä ohjelmaan ja kokeilemalla sen käyttöä.
Pienen stresstestin aikana löysin ongelman siinä kun toistaa tason generointia useamman kerran peräkkäin.

Perjantaina sain vertaispalautteen erittäin kattavaksi ja olin tyytyväinen tuloksiini. Aloin myös implementoimaan testausta wfc luokalle.
Testauksen laajennus eteni ilman ongelmia ja keksin mielestäni järkeviä tapoja testata ohjelman toimivuutta sen satunnaisuudesta huolimatta.
Tämä onnistui hallitsemalla satunnaisuutta rajoittamalla wfc algoritmin vaihtoehtoja eri tilanteissa.
katsoin myös certaispalutteen ja otin huomioon saamaani palutetta, ja tein korjauksia.

Lauantaina minulla oli hieman aikaa projektille, joten päätin implementoida korjauksen vertaisarvioinnissa mainitulle bugille.
Lisäksi alointin suunnittelun patch funktiolle, joka täyttää viimeiset tyhjät kohdat generioinnin lopuksi jos niitä jää.

## aikataulu:
| pv  | tuntimäärä | aihe                                           |
| --- | ---------- | ---------------------------------------------- |
| ma  |            |                                                |
| ti  | 1          | vertaisarvion aloitus                          |
| ke  |            |                                                |
| to  |            |                                                |
| pe  | 4          | vertaisarvion viimeistely ja testien laajennus |
| la  | 1          | wfc viimeistely                                |