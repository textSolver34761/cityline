import pandas as pd

data = pd.read_json(r'paris_lines_systems_and_modes.json')

data_wiki = pd.read_html('https://fr.wikipedia.org/wiki/M%C3%A9tro_de_Paris') 
dataFrame_wiki = data_wiki[1]