import pandas as pd
import os
# Test round
manuals_df = pd.read_excel("/Users/phillipscitp/Desktop/CITP-Portal/Green Tea Extract/2.0_P3_manuals.xlsx")
manuals_output = pd.read_excel("/Users/phillipscitp/Desktop/CITP-Portal/output_manuals.xlsx")
manuals_id_num = pd.merge(manuals_df, manuals_output, on="PlateID")
# manuals_id_num.to_excel("manuals_with_exp_id.xlsx")
# Merge function for adding ExperimentID to all dataframes
def merge(xlsx1: str, xlsx2: str, desired_filename: str): # xlsx1 and xlsx2 are string file paths for df conversion
    df1 = pd.read_excel(xlsx1)
    df2 = pd.read_excel(xlsx2)
    df3 = pd.merge(df1, df2, on="PlateID")
    df3.to_excel(f"{desired_filename}.xlsx")
# merge("/Users/phillipscitp/Desktop/CITP-Portal/ALM data/ALM_NP1_PG_RVL_sorted_columns.xlsx", "/Users/phillipscitp/Desktop/CITP-Portal/output_alm.xlsx", "alm_NP1_exp_id")

# assign directory
directory = "insert_name_here"
output_file = "insert_name_here"
merged_filename = "insert_name_here"
# iterate over files in that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        merge(f, output_file, merged_filename)
