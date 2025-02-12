import pandas as pd

df = pd.read_csv('D:/fire_data/final_analysis/scrub_data.csv')

df['extreme'] = df["hazard_1"].apply(lambda x: 1 if  x > 0.137872 else 0)
df['moderate'] = df["hazard_1"].apply(lambda x: 1 if .001911 < x <= .137872 else 0)
df['low'] = df["hazard_1"].apply(lambda x: 1 if x <= .001911 else 0)
df.to_csv('D:/fire_data/final_analysis/scrub_data.csv')
print(df.describe())
