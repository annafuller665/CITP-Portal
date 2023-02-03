import pandas as pd
import os
import glob
# use glob to get all the csv files in the folder
path = os.getcwd()
csv_files = glob.glob(os.path.join(path, "*xlsx"))
 # loop over the list of csv files
for f in csv_files:
    
    # read the csv file
    df = pd.read_excel(f)
      
print(df)




