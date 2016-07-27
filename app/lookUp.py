import pandas as pd

characters = ["", "Alex", "Akuma", "Chun Li", "Dudley", "Elena", "Hugo", "Ibuki", "Ken", 
"Makoto", "Necro", "Oro", "Q", "Remy", "Ryu", "Sean", "Twelve", "Urien", "Yang", "Yun"]

try: data = pd.read_csv("3rd Strike/3rdStrikeWebsite/app/city-region.csv") #Pythonanywhere path
except: data = pd.read_csv("app/city-region.csv")
else: print("Couldn't find data...")

cities = data["City"]
city_dict = {k:v for k, v in zip(data["City"], data["Region"])}