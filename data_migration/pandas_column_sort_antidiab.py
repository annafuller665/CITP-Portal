"""
Sorting lifespan tables by tech number
"""
import pandas as pd

# Sorting the table by tech
df = pd.read_csv(r'~/Desktop/CITP-Portal/data_migration/antidiab_lifespan-Table 1.csv')
df.sort_values('Tech').to_excel('antidiab_lifespan-Table 1_sorted.xlsx')

# Creating list of all strains present
strains_list = df["Strain"].tolist()
strains = []
for name in range(len(strains_list)):
    if strains_list[name] not in strains:
        strains.append(strains_list[name])
#print(strains)
# All strains match

# Creating list of all compounds present
compounds_list = df["Compound"].tolist()
compounds = []
for comp in range(len(compounds_list)):
    if compounds_list[comp] not in compounds:
        compounds.append(compounds_list[comp])
#print(compounds)
# All compounds match
