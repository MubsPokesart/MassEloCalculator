# MassEloCalculator

Creation Date: 2021-9-13

## What is MassEloCalculator? What does it do?  

MassEloCalculator was one of my first completely file-based projects with regards to the python language. Most of my projects prior to MassEloCalculator were primarily based on user inputs.

In short, MassEloCalculator mass performs the ELO calculation utilized by many ladder-based head to head games. [BZStrats’s explanation]([http://bzstats.strayer.de/bzinfo/elo/?lang=en](http://bzstats.strayer.de/bzinfo/elo/?lang=en)) can give notable information about how ELO works.

[Heres a full google spreadsheet]([https://docs.google.com/spreadsheets/d/1n55zHEuDbF0WuuAwqL0TyD0i5e-FlCD4p26TKmOUwPQ/edit#gid=0](https://docs.google.com/spreadsheets/d/1n55zHEuDbF0WuuAwqL0TyD0i5e-FlCD4p26TKmOUwPQ/edit#gid=0)) that showcases how the outputs of the program can be useful.

## Functionality

The mass calculation of ELO is performed by first generating lists of file inputs given by the user. There are four files at play here.

- `namelist.txt` and `elolist.txt` are files that work off each other. The former provides all the names of all the participants in a given ladder, and the latter gives corresponding ELO ratings, which start at 1000 for my purposes.

- `roundwinners.txt` and `roundlosers.txt` work off each other in the sense that they provide both the winners and losers in a given sequence of ELO calculations.

Here is an example of these things in play:

**namelist.txt**
```
Nalei
Freezerman
lvl100Blaziken
Saber (PGO)
Astrologistic style
Peary
Rellia
WillRBX
L pichon
DMPancake
```
**elolist.txt**
```
1000
1000
1000
1000
1000
1000
1000
1000
1000
1000
```
Lets use this, as an example for roundwinners and roundlosers:

**roundwinners.txt**
```
Peary
Rellia
WillRBX
L pichon
DMPancake
```
**roundlosers.txt**
```
Nalei
Freezerman
lvl100Blaziken
Saber (PGO)
Astrologistic style
```
If you run the program in an IDE of your choice with these preset inputs, it will do a few things. First, it will put these inputs into lists, or arrays. Then, it will check to see if both of the sets of parallel lists have the same amount of elements. If true, it will run the program and give an output such as this:

**Console**
```
ELO CHANGES:
Peary: 1000 -> 1050
Nalei: 1000 -> 950
ELO CHANGES:
Rellia: 1000 -> 1050
Freezerman: 1000 -> 950
ELO CHANGES:
WillRBX: 1000 -> 1050
lvl100Blaziken: 1000 -> 950
ELO CHANGES:
L pichon: 1000 -> 1050
Saber (PGO): 1000 -> 950
ELO CHANGES:
DMPancake: 1000 -> 1050
Astrologistic style: 1000 -> 950
```


**elolist.txt**
```
950
950
950
950
950
1050
1050
1050
1050
1050
```
**changelog.txt**
```
CHANGELOG.TXT 
STUFF AFTER THIS
_______________________

MATCH: Peary vs Nalei
Peary won

ELO CHANGES:
Peary: 1000 -> 1050
Nalei: 1000 -> 950

MATCH: Rellia vs Freezerman
Rellia won

ELO CHANGES:
Rellia: 1000 -> 1050
Freezerman: 1000 -> 950

MATCH: WillRBX vs lvl100Blaziken
WillRBX won

ELO CHANGES:
WillRBX: 1000 -> 1050
lvl100Blaziken: 1000 -> 950

MATCH: L pichon vs Saber (PGO)
L pichon won

ELO CHANGES:
L pichon: 1000 -> 1050
Saber (PGO): 1000 -> 950

MATCH: DMPancake vs Astrologistic style
DMPancake won

ELO CHANGES:
DMPancake: 1000 -> 1050
Astrologistic style: 1000 -> 950
```

