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
dataFrame_wiki.loc[
    (dataFrame_wiki['Ligne Horizon']=='NAN') & 
    (dataFrame_wiki['Parcours']=='La Défense ↔ Château de Vincennes') & 
    (dataFrame_wiki['Mise en service']==1990) & 
    (dataFrame_wiki['Dernier prolongement']==1992) &
    (dataFrame_wiki['Longueur en km (en surface)']=='16,6' '(0,6)') &
    (dataFrame_wiki['Nombre de stations']==25) &
    (dataFrame_wiki['Materiel']=='MP 05') &
    (dataFrame_wiki['Voitures par rame']==6) &
    (dataFrame_wiki.iloc[['Nb de Rames'==45]]) &
    (dataFrame_wiki['Nb total de rames'==56]) &
    (dataFrame_wiki['Millions de voyageurs (2017)'==181,2])
    ] = [['M 1','La Défense ↔ Château de Vincennes',1990,1992,16.6,25,'MP 05',6,45,56,181.2]]



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

