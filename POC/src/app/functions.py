#Import Libraries
import PyPDF2
import re
import os
from PyPDF2 import PdfReader
from pyresparser import ResumeParser
import warnings
import logging

# Configure logging to write to a text file
logging.basicConfig(filename='error_log.txt', level=logging.ERROR)

from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import (
        TextAnalyticsClient,
        ExtractiveSummaryAction
    ) 

key = "6d45ac78cd7e4cda97822052bdd170e2"
endpoint ="https://hirebolt.cognitiveservices.azure.com/"

def get_file_paths(folder_path):
    # Get a list of all files in the specified folder
    file_paths = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))]
    return file_paths

def get_text(filepath):
    reader = PdfReader(filepath)
    content_info = []
    no_of_pages = len(reader.pages)
    
    for i in range(no_of_pages):
        page = reader.pages[i]
        content_info.append(page.extract_text().lower())

    if content_info ==[''] :
        content_info.clear()
        content_info.append('Not able to extract')
       
    
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
        pattern = r"\+91\s?\d\s?\d{9}|\+91-\d{10}|\d{10}|\(\+91\)\s?\d{3}\s?\d{3}\s?\d{4}"
        
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


def sample_extractive_summarization(client,document):



    poller = client.begin_analyze_actions(
        document,
        actions=[
            ExtractiveSummaryAction(max_sentence_count=20)
        ],
    )

    document_results = poller.result()
    for result in document_results:
        extract_summary_result = result[0]  # first document, first result
        if extract_summary_result.is_error:
            print("...Is an error with code '{}' and message '{}'".format(
                extract_summary_result.code, extract_summary_result.message
            ))
        else:
            print("Summary extracted: \n{}".format(
                " ".join([sentence.text for sentence in extract_summary_result.sentences]))
            )

    return [sentence.text for sentence in extract_summary_result.sentences]


def get_skills(filepath):
    data = ResumeParser(filepath).get_extracted_data()
    return data['skills']


def authenticate_client():
    ta_credential = AzureKeyCredential(key)
    text_analytics_client = TextAnalyticsClient(
            endpoint=endpoint, 
            credential=ta_credential)
    return text_analytics_client
