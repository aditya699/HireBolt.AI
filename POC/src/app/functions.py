#Import Libraries
import PyPDF2
import re
from PyPDF2 import PdfReader

# To get the phone number from resume
def get_phone_number(filepath: str) -> str:
    reader = PdfReader(filepath)
    content_info = []
    no_of_pages = len(reader.pages)
    
    for i in range(no_of_pages):
        page = reader.pages[i]
        content_info.append(page.extract_text())
    

        # Modified regex pattern to allow spaces in the phone number
        pattern = r"\+91\s?\d\s?\d{9} | \+91-d{10}"
        
        # Using findall to get all matches in the content
        results = re.findall(pattern, content_info[i])
        
        # Check if there are any matches
        if results:
            for match in results:
                return match


# To get the phone number from resume
def get_email_id(filepath: str) -> str:
    reader = PdfReader(filepath)
    content_info = []
    no_of_pages = len(reader.pages)
    
    for i in range(no_of_pages):
        page = reader.pages[i]
        content_info.append(page.extract_text())
    

        # Modified regex pattern to allow spaces in the phone number
        pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
        
        # Using findall to get all matches in the content
        results = re.findall(pattern, content_info[i])
        
        # Check if there are any matches
        if results:
            for match in results:
                return match
