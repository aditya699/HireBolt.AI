'''
Author -Aditya Bhatt 8:00 AM 28/01/2023 
Objective-
1.Create a application for resume selection
'''
filepaths=[]


# Specify the folder path
folder_path = "C:/Users/aditya/Desktop/2024/HireBolt.AI/Data"


#Import Modules
import abc
from functions import get_phone_number
from functions import get_email_id
from functions import sample_abstractive_summarization
from functions import get_text,get_file_paths
import numpy as np
import pandas as pd
#Call the functions

# Get file paths in the folder
file_paths = get_file_paths(folder_path)

# Print the file paths
for file_path in file_paths:
    filepaths.append(file_path)
a=pd.DataFrame()
for filepath in filepaths:

    phone_number=get_phone_number(filepath)
    email_id=get_email_id(filepath)
    text=get_text(filepath)
    summary=sample_abstractive_summarization(document=text)
    # print(summary)
    # print(phone_number)
    # print(email_id)
    a=a.append({'phone_number':[phone_number],'email_id':[email_id],'summary':[summary]},ignore_index=True)
    a.to_csv("Appliciants.csv")
# print(a.head())



