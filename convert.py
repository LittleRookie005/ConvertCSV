import pandas as pd 
read_file = pd.read_excel ("filename_import.xlsx") 

read_file.to_csv ("R17.csv",  
                  index = None, 
                  header=True) 
df = pd.DataFrame(pd.read_csv("filename_export.csv")) 

df
