#! /usr/bin/python3
import pandas as pd
xl = pd.ExcelFile('book1.xlsx')
# get the first sheet as an object
df = pd.read_excel(xl, 0, header=None)
print(df.head())