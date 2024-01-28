'''
Author -Aditya Bhatt 8:00 AM 28/01/2023 
Objective-
1.Create a application for resume selection
'''
filepath="C:/Users/aditya/Desktop/2024/HireBolt.AI/POC/Aditya Bhatt CV.pdf"
#Import Modules
from functions import get_phone_number
from functions import get_email_id
from functions import sample_abstractive_summarization
from functions import get_text
#Call the functions
print(get_phone_number(filepath))
print(get_email_id(filepath))
text=get_text(filepath)
print(sample_abstractive_summarization(document=text))



