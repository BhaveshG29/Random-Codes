import pandas as pd

bios = pd.read_csv("complete-pandas-tutorial/data/bios.csv")
bios.index = bios["athlete_id"]

print(bios.loc[12:20, ["name", "born_date", "died_date"]])

coffee_data = pd.read_csv("complete-pandas-tutorial/data/coffee.csv")
coffee_data.index = pd.RangeIndex(start=1, stop=len(coffee_data)+1)
print("\n\n", coffee_data.loc[:,["Day", "Units Sold"]])


print("\n\n", coffee_data.sort_values(["Units Sold", "Coffee Type"], ascending=[0,1]))
