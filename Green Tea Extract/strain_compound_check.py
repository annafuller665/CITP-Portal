import pandas as pd
df_tox = pd.read_csv("2.0_P1_tox_screen.csv")
strains_tox = df_tox["Worm Strain from plate"]
# Strains check
strain_tox = []
for item in strains_tox:
    if item not in strain_tox:
        strain_tox.append(item)
# print(strain_tox) All present
df_manuals = pd.read_csv("2.0_P3_manuals.csv")
strains_manuals = df_tox["Worm Strain from plate"]
strain_manuals = []
for item in strains_manuals:
    if item not in strain_manuals:
        strain_manuals.append(item)
# print(strain_manuals) All present

# Compounds check
comps_tox = df_tox["Drug for Plate"]
comp_tox = []
for item in comps_tox:
    if item not in comp_tox:
        comp_tox.append(item)
# print(comp_tox) All present

comps_manuals = df_manuals["Drug for Plate"]
comp_manuals = []
for item in comps_manuals:
    if item not in comp_manuals:
        comp_manuals.append(item)
# print(comp_manuals) All present
