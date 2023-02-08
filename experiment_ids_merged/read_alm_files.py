
import os
import pandas as pd
import re

# assign directory
directory = "alm_fm_sorted"

# create a master ID table with two columns
id_table = pd.DataFrame({"PlateID":[], "ExperimentID":[]})
# filename number extraction
def get_numbers_from_filename(filename):
    return re.search(r'\d+', filename).group(0)

# iterate over files in that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        # print the filename in the terminal
        print(f)
        # load the file into a pandas frame
        excel_data_df = pd.read_excel(f, sheet_name=0)
        unique_ids = []
        for id in excel_data_df["PlateID"]:
            if id not in unique_ids:
                unique_ids.append(id)
        # make a list of unique PlateID's that appear in the file
        temp_df = pd.DataFrame()
        temp_df["PlateID"] = unique_ids
        temp_df["ExperimentID"] = get_numbers_from_filename(filename)
        id_table = pd.concat([id_table, temp_df])
        id_table.reset_index(drop = True)


id_table.to_excel("output_alm.xlsx")


        # make a temporary data frame:
            # first column: the list of unique PlateID's
            # second column: the filename repeated in each row - only the number!
        # append this temp table to the master ID table