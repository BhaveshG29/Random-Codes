import pandas as pd


df1 = pd.DataFrame([[1,2,3], [16, 32, 48], [12, 24, 36]], columns=["A", "B", "C"], index=[1,2,3], dtype="int16")

print("DataFrame")
print(df1,"\n")
print(" Describes the DataFrame.")
print(df1.describe(), "\n")
print("Info of DataFrame.")
print(df1.info(), "\n")
print("Prints 1st two Rows.")
print(df1.head(2), "\n")
print("Prints Last Row")
print(df1.tail(1))

