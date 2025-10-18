import pandas as pd


coffee_data = pd.read_csv("complete-pandas-tutorial/warmup-data/coffee.csv")
coffee_data.index = pd.RangeIndex(start=1, stop=len(coffee_data)+1)

print(coffee_data, "\n\n")

results1 = pd.read_parquet("complete-pandas-tutorial/data/results.parquet")
results1.index = pd.RangeIndex(start=1, stop=len(results1)+1)
print(results1.head())


results2 =  pd.read_csv("complete-pandas-tutorial/data/results.csv")
print(results2.head())
 
