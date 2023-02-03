import pandas as pd
df_ThioT = pd.read_excel("ALM_AKG_ThioT_using.xlsx")
columns_list_ThioT = list(df_ThioT.columns)
df_baseline = pd.read_excel("ALM_baseline.xlsx")
columns_list_baseline = list(df_baseline.columns)
df_NP1 = pd.read_excel("ALM_NP1_PG_RVL.xlsx", sheet_name=1)
columns_list_PD1 = list(df_NP1.columns)
df_template = pd.read_excel("ALM_template.xlsx")
columns_list_template = list(df_template.columns)
all_headers = [columns_list_ThioT, columns_list_baseline, columns_list_PD1]
compounds_baseline = df_baseline["Compound"].tolist()
compounds_NP1 = df_NP1["Compound"].tolist() # All untreated
NP1_no_repeats = []
for item in compounds_NP1:
    if item not in NP1_no_repeats:
        NP1_no_repeats.append(item)

# print(NP1_no_repeats) All present in table

sorted_df_ThioT = df_ThioT.sort_values("Strain")
list_strains_ThioT = []
for item in sorted_df_ThioT["Strain"]:
    if item not in list_strains_ThioT:
        list_strains_ThioT.append(item)
# print(list_strains_ThioT) All strains present in table







