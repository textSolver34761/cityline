import pandas as pd

# parse according to "system_name":"Métro de Paris"
# asked help on StackOverflow :
#https://stackoverflow.com/questions/65328899/is-there-a-way-to-sort-a-dataframe-using-pandas-or-other-library-in-python
data = pd.read_json(r'paris_lines_systems_and_modes.json')
data = data[data.system_name == "Métro de Paris"]
data = data[data.color != "#000"]
print(data)

# parse wiki table
data_wiki = pd.read_html('https://fr.wikipedia.org/wiki/M%C3%A9tro_de_Paris')
dataFrame_wiki = data_wiki[1]
print(dataFrame_wiki)

# looking for a way to replace NAN by M1, M2 etc. (content)
#  looking for a way to replace Ligne by Ligne Horizon. (header)

# https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html#database-style-dataframe-or-named-series-joining-merging

# parse wiki table 
dem_paris = pd.read_html('https://fr.wikipedia.org/wiki/Mod%C3%A8le:Tableau_D%C3%A9mographie_Paris#Carte')
df_dem_paris_250_1600 = dem_paris[0]
df_dem_paris_1637_1811 = dem_paris[1]
df_dem_paris_1817_1866 = dem_paris[2]
df_dem_paris_1872_1911 = dem_paris[3]
df_dem_paris_1921_1975 = dem_paris[4]
df_dem_paris_1982_2016 = dem_paris[5]

