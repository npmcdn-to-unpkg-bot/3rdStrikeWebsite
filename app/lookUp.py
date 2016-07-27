import pandas as pd

characters = ["", "Alex", "Akuma", "Chun Li", "Dudley", "Elena", "Hugo", "Ibuki", "Ken", 
"Makoto", "Necro", "Oro", "Q", "Remy", "Ryu", "Sean", "Twelve", "Urien", "Yang", "Yun"]

data = pd.read_csv("app/city-region.csv")

cities = data["City"]
city_dict = {k:v for k, v in zip(data["City"], data["Region"])}