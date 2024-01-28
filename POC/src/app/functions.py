#Import Libraries
import PyPDF2
import re
from PyPDF2 import PdfReader

key = "6d45ac78cd7e4cda97822052bdd170e2"
endpoint ="https://hirebolt.cognitiveservices.azure.com/"

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential


def get_text(filepath):
    reader = PdfReader(filepath)
    content_info = []
    no_of_pages = len(reader.pages)
    
    for i in range(no_of_pages):
        page = reader.pages[i]
        content_info.append(page.extract_text())
    
    return content_info

# To get the phone number from resume
def get_phone_number(filepath: str) -> str:
    reader = PdfReader(filepath)
    content_info = []
    no_of_pages = len(reader.pages)
    
    for i in range(no_of_pages):
        page = reader.pages[i]
        content_info.append(page.extract_text())
    

        # Modified regex pattern to allow spaces in the phone number
        pattern = r"\+91\s?\d\s?\d{9} | \+91-d{10} | \d{10}"
        
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

# This example requires environment variables named "LANGUAGE_KEY" and "LANGUAGE_ENDPOINT"




def sample_abstractive_summarization(document) :

    text_analytics_client = TextAnalyticsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key),
    )
    poller = text_analytics_client.begin_abstract_summary(document)
    abstract_summary_results = poller.result()
    result_summary=[]
    for result in abstract_summary_results:
        if result.kind == "AbstractiveSummarization":
            for summary in result.summaries:
                result_summary.append(summary.text)

    return result_summary