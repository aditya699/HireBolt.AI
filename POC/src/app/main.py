'''
Author -Aditya Bhatt 8:00 AM 28/01/2023 
Objective-
1.Create a application for resume selection
'''
filepath="C:/Users/aditya/Desktop/2024/HireBolt.AI/POC/Aditya Bhatt CV.pdf"
#Import Modules
import abc
from functions import get_phone_number
from functions import get_email_id
from functions import sample_abstractive_summarization
from functions import get_text
import numpy as np
import pandas as pd
#Call the functions

phone_number=get_phone_number(filepath)
email_id=get_email_id(filepath)
text=get_text(filepath)
summary=sample_abstractive_summarization(document=text)
summary=','.join(summary)
print(summary)
print(phone_number)
print(email_id)
# a=pd.DataFrame({'phone_number':phone_number,'email_id':email_id,'summary':summary})
# a.to_csv("Appliciants.csv")
# print(a.head())



