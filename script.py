import pandas as pd

data = pd.read_json(r'paris_lines_systems_and_modes.json')

data_wiki = pd.read_html('https://fr.wikipedia.org/wiki/M%C3%A9tro_de_Paris') 
dataFrame_wiki = data_wiki[1]

dem_paris = pd.read_html('https://fr.wikipedia.org/wiki/Mod%C3%A8le:Tableau_D%C3%A9mographie_Paris#Carte')
df_dem_paris_250_1600 = dem_paris[0]
df_dem_paris_1637_1811 = dem_paris[1]
df_dem_paris_1817_1866 = dem_paris[2]
df_dem_paris_1872_1911 = dem_paris[3]
df_dem_paris_1921_1975 = dem_paris[4]
df_dem_paris_1982_2016 = dem_paris[5]

