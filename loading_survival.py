import pandas as pd
df_csv = pd.read_csv("metfo_sum_tech-Table 1.csv")
#print(df_csv)
df = pd.DataFrame(df_csv)
print(df)