import pandas as pd

# parse according to "system_name":"Métro de Paris"
# asked help on StackOverflow :
#https://stackoverflow.com/questions/65328899/is-there-a-way-to-sort-a-dataframe-using-pandas-or-other-library-in-python
data = pd.read_json(r'paris_lines_systems_and_modes.json')
data = data[data.system_name == "Métro de Paris"]
data = data[data.color != "#000"]
#print(data)

# parse wiki table
data_wiki = pd.read_html('https://fr.wikipedia.org/wiki/M%C3%A9tro_de_Paris')
dataFrame_wiki = data_wiki[1]

# looking for a way to replace Ligne by Ligne Horizon. (header)
dataFrame_wiki.columns = ['Ligne Horizon','Parcours','Mise en service','Dernier prolongement','Longueur en km (en surface)','Nombre de stations','Materiel','Voitures par rame','Nb de Rames','Nb total de rames','Millions de voyageurs (2017)']

# looking for a way to replace NAN by M1, M2 etc. (content)
dataFrame_wiki.loc[0,'Ligne Horizon']='M 1'
dataFrame_wiki.loc[1,'Ligne Horizon']='M 2'
dataFrame_wiki.loc[2,'Ligne Horizon']='M 3'
dataFrame_wiki.loc[3,'Ligne Horizon']='M 3bis'
dataFrame_wiki.loc[4,'Ligne Horizon']='M 4'
dataFrame_wiki.loc[5,'Ligne Horizon']='M 5'
dataFrame_wiki.loc[6,'Ligne Horizon']='M 6'
dataFrame_wiki.loc[7,'Ligne Horizon']='M 7'
dataFrame_wiki.loc[8,'Ligne Horizon']='M 7bis'
dataFrame_wiki.loc[9,'Ligne Horizon']='M 8'
dataFrame_wiki.loc[10,'Ligne Horizon']='M 9'
dataFrame_wiki.loc[11,'Ligne Horizon']='M 10'
dataFrame_wiki.loc[12,'Ligne Horizon']='M 11'
dataFrame_wiki.loc[13,'Ligne Horizon']='M 12'
dataFrame_wiki.loc[14,'Ligne Horizon']='M 13'
dataFrame_wiki.loc[15,'Ligne Horizon']='M 14'


print(dataFrame_wiki)

# https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html#database-style-dataframe-or-named-series-joining-merging

# parse wiki table 
dem_paris = pd.read_html('https://fr.wikipedia.org/wiki/Mod%C3%A8le:Tableau_D%C3%A9mographie_Paris#Carte')
df_dem_paris_250_1600 = dem_paris[0]
df_dem_paris_1637_1811 = dem_paris[1]
df_dem_paris_1817_1866 = dem_paris[2]
df_dem_paris_1872_1911 = dem_paris[3]
df_dem_paris_1921_1975 = dem_paris[4]
df_dem_paris_1982_2016 = dem_paris[5]

