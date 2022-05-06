# Cityline
**Français** : <br />
**Présentation du projet** <br />

Le but est d'analyser l'expantion du métro en fonction de l'expansion de Paris (habitants, déplacements, etc.) <br />

**TODO** <br />
Dans un premier temps, trouver les dates de mises en services fiables pour les faire coïcider avec les données de citylines : **fait** <br />
Dans un second temps, trouver des documents permettant l'analyse de l'expansion de Paris (habitants, déplacements, etc.) **fait** <br />
<br />
Prendre les données au format JSON de citylines et ne répcupérer les données liés au métro. **fait** <br />
Faire de même pour les données du tableau wikipedia. **fait** <br />
<br>
Concaténer les données entre elles de façon à n'avoir qu'un JSON avec les données du JSON "initial", (paris_lines_systems_and_modes.json) et les données du tableau wikipedia. **fait** <br />
<br />
Créer une carte de Paris avec une librairie. (Laquelle?) <br />
Combiner la carte et les données (format JSON  ou DataFrame) pour voir la donnée : data Viz. <br />
Ajouter une barre de temps pour que l'utilisateur puisse faire défiler les années et que les données puissent être interactifs  <br />
(par ex : si "bare de temps" est sur 2030, la ligne 15 du métro de Paris apparait)

**Données analysés** <br />
Une partie des données est issue du site citylines. Ces données se trouvent [ici](https://www.citylines.co/data?city=paris#city "Cityline"). <br />
Une autre partie des données proviennent de [Wikipédia](https://fr.wikipedia.org/wiki/M%C3%A9tro_de_Paris "Wikipedia") (tableau avec les dates de mises en services). <br />
Des données démographique proviennent également de [Wikipédia](https://fr.wikipedia.org/wiki/Mod%C3%A8le:Tableau_D%C3%A9mographie_Paris) <br />

**Fichiers contenus dans le projet**
- gitignore <br />
- paris_lines_systems_and_modes.json : tous les systèmes et moyens de transports dans Paris <br />
- paris_stations.geojson  <br />
- paris_section.geojson <br />
- script.py <br />
- script.ipynb (Le fichier script.py convertie en un Jupyter Notbook) <br />
- secrutity.md 

**Fonctionnement du programme** <br />

**Technologie utilisé** <br />
- python <br />
- spark

**Imports natif** <br />
- pandas <br />
- pyspark <br />

**Axes d'amélioration** <br />

**Auteur**<br />
Benjamin PRADON

<hr>

**English** : <br />
**Project**

The goal is to analyze the expansion of Paris' metro according to the expansion of Paris (inhabitants, movements, etc.)

**TODO** <br>
First, find the dates of reliable commissioning to make them coincide with the citylines data: **done** <br>

Secondly, finding documents allowing the analysis of the expansion of Paris (inhabitants, displacements, etc.) **done**

Take data in JSON format from citylines and do not retrieve data related to the metro. **done** <br />
Do the same for the data in the wikipedia table. **done** <br />

Concatenate the data between them so as to have only one JSON with the data of the "initial" JSON, (paris_lines_systems_and_modes.json) and the data of the wikipedia table. **done** <br />
<br />
Create a map of Paris using a library (which one?) <br />
Combine the map and data (JSON JSON  or DataFrame) to see the data: data Viz. <br />
Add a barre of time for the user to be able to make the years pass and that data are interactive. <br />
(eg : if the  "time barre " displays 2030, the map will display the line 15 of the Paris métro)

**Analyzed data** <br/>
Part of the data comes from the citylines site. This data can be found [here](https://www.citylines.co/data?city=paris#city "Cityline"). <br />
Another part of the data provided by [Wikipedia](https://fr.wikipedia.org/wiki/M%C3%A9tro_de_Paris "Wikipedia")
Wikipedia (table with the dates of commissioning). <br />
Demographic data also provided from [Wikipedia](https://fr.wikipedia.org/wiki/Mod%C3%A8le:Tableau_D%C3%A9mographie_Paris) <br />

**Files in the project**

**How does the program works**

**Technology used**

**Native imports**

**Areas for improvement**

**Author** <br />
Benjamin PRADON
