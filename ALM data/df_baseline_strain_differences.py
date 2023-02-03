import pandas as pd
df_baseline = pd.read_csv("ALM_baseline_sorted_columns.csv")
strains = df_baseline["Worm Strain from plate"]
strains_list = []
for item in strains:
    if item not in strains_list:
        strains_list.append(item)
print(strains_list)