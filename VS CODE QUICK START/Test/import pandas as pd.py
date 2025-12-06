import pandas as pd

df = pd.read_csv(r"C:\Users\Redal\OneDrive\Desktop\Travel euro\FashionDataset.csv")
print(df)



df1 = df.drop(columns="Unnamed: 0", inplace=True)
print(df1)
