# Projekt 3 - Stahování výsledků voleb
<b>Popis</b><br><br>
Program stahuje informace o volbách a následně jej ukládá do *.csv souboru. Je potřeba vložit odkaz a název souboru<br><br>
<b>Instalace knihoven</b><br><br>
$ pip install requests<br>
$ pip install <br>
$ pip install beautifulsoup4<br><br>
<b>Použití</b><br><br>
Je potřeba vložit dva argumenty, první je odkaz z <a href="https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ" target="_blank">této webové stránky</a> z odkazu X ve sloupci "Výběr obce"<br><br>
Argument1: Odkaz z pole X <br>
Argument2: Název souboru (bez .csv) <br>
Spuštění: $ volbostahovac.py "argument1" "argument2"<br><br>
<b>Ukázka běhu</b><br><br>
(venv) D:\Projekty\Python\Projekt_3>main.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=3&xnumnuts=3106" "strakonice"<br>
Spouštím stahování dat<br>
Ukládám do souboru<br>
Dokončeno - soubor strakonice.csv<br>
</table>
