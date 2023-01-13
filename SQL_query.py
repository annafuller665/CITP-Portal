from pathlib import Path
import os
import pandas as pd
import psycopg2

conn = psycopg2.connect(
    dbname=DBNAME, user=USER, password=PWD, host=HOST, port=PORT
)

c = conn.cursor()

# COMPOUNDS

query = (
    "SELECT comp_id, comp_name, comp_abbr, control_name FROM all_compounds_table"
)

c.execute(query)
res = c.fetchall()

all_compounds_table = pd.DataFrame.from_records(
    res,
    columns=["comp_id", "comp_name", "comp_abbr", "control_name"],
)

query = "SELECT comp_id, alternate_comp_name FROM compound_reference_table"

c.execute(query)
res = c.fetchall()

compound_reference_table = pd.DataFrame.from_records(
    res,
    columns=["comp_id", "alternate_comp_names"],
)

c.close()
conn.close()

'''
CSV File Database Transfer Steps:
c = conn.cursor()
query = "SELECT comp_id, comp_name, comp_abbr, control_name FROM all_compounds_table"
  
c.execute(query)
  
res = c.fetchall()
  
res
# Pandas Dataframe without column names

df = pd.DataFrame(res)
  
df

# Pandas Dataframe with column names

columns = ["comp_id", "comp_name", "comp_abbr", "control_name"]
  
df = pd.DataFrame(res, columns = columns)
  
df

# CSV file conversion
import csv
input_variable = "df"
with open('Example.csv', 'w', newline = '') as csvfile:
    my_writer = csv.writer(csvfile, delimiter = ' ')
    my_writer.writerow(input_variable)
df.to_csv("df.csv", index=False)
'''
