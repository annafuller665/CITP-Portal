import pandas as pd
import os
import glob

# Running for loop!
# use glob to get all the csv files 
# in the folder
path = os.getcwd()
csv_files = glob.glob(os.path.join(path, "*.csv"))
  
  
# loop over the list of csv files
for f in csv_files:
      
    # read the csv file and column headers
    df = pd.read_csv(f)
    my_list=list(df.columns)

      
    # print the location and filename
    print('Column Headers', my_list)
    print('File Name:', f.split("\\")[-1])


# Filereader function
# use glob to get all the csv files in the folder
def csv_file_reader():
    path = os.getcwd()
    csv_files = glob.glob(os.path.join(path, "csv"))
    headers_list = []
    # loop over the list of csv files
    for f in csv_files:
    # read the csv file
        df = pd.read_csv(f)
        my_list = list(df.columns)

    # print the location and filename
    print('Column Headers', my_list)
    print('File Name:', f.split("\\")[-1])
headers = csv_file_reader()







# Other attempts
# Column reader function
def column_reader(file_name: str) -> str:
    df = pd.read_csv(file_name)
    headers = list(df.columns.values)
    return headers, file_name
    # return file_name
    
# Test print(column_reader("metfo_lifespan-Table1.csv"))
def all_files(file_type, path = os.getcwd()):
    csv_files = glob.glob(os.path.join(path, file_type))
    column_headers = []
    file_names = []
    for f in csv_files:
        file_names.append(f)
        column_headers.append(column_reader(f))
    return column_headers, file_names
# Test print(all_files("csv", path = os.getcwd()))


      
    