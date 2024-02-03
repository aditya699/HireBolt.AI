import streamlit as st
import re
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import pandas as pd
from functions import get_phone_number, get_email_id, sample_extractive_summarization, get_text, get_file_paths,get_skills,authenticate_client
import logging

client=authenticate_client()
# Function to clean text
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text

# Function to calculate cosine similarity
def calculate_similarity(query_vector, document_matrix):
    cosine_similarities = cosine_similarity(query_vector, document_matrix)
    return cosine_similarities.flatten()

# Streamlit UI
def main():
    st.title("Hire4Bharat.AI")

    try:

        # Input fields
        folder_path = st.text_input("Enter the folder path:")
        folder_path=folder_path.replace('\\','/')
        job_description = st.text_area("Enter the job description:")
        no_of_candidates = st.number_input("Number of candidates to select:", min_value=1, step=1, value=5)

        # Process button
        if st.button("Process Resumes"):
            filepaths = []
            a = pd.DataFrame()
            z = pd.DataFrame()

            # Get file paths in the folder
            file_paths = get_file_paths(folder_path)

            # Process resumes
            for filepath in file_paths:
                phone_number = get_phone_number(filepath)
                email_id = get_email_id(filepath)
                text = get_text(filepath)
                summary = sample_extractive_summarization(client,document=text)
                skills=get_skills(filepath)
                a = a.append({'phone_number': [phone_number], 'email_id': [email_id], 'summary': [summary],'file_paths':[filepath],'skills':[skills]}, ignore_index=True)
                z=z.append({'text_extracor':[text],'file_path':[filepath]}, ignore_index=True)

            z.to_csv("full_extractor.csv")
            a.to_csv("Candidates.csv")
            # Clean and preprocess data
            a=pd.read_csv("Candidates.csv")
            a.drop("Unnamed: 0", axis=1, inplace=True)
            a['summary'] = a['summary'].apply(lambda x: x[3:-3] if type(x) is str and len(x) >= 6 else x)
            a['cleaned_summary'] = a['summary'].apply(clean_text)

            # TF-IDF Vectorization
            vectorizer = TfidfVectorizer(stop_words='english')
            tfidf_matrix = vectorizer.fit_transform(a['cleaned_summary'])

            # Define job description
            cleaned_job_description = clean_text(job_description)
            job_description_vector = vectorizer.transform([cleaned_job_description])

            # Calculate cosine similarity
            a['similarity_score'] = calculate_similarity(job_description_vector, tfidf_matrix)

            # Sort the dataframe based on similarity scores
            df_sorted = a.sort_values(by='similarity_score', ascending=False)

            # Save the selected applicants to a CSV file
            df_sorted.head(no_of_candidates).to_csv("selected_applicants.csv", index=False)

            # Display selected applicants
            st.success("Resumes processed successfully!")
            st.dataframe(df_sorted.head(no_of_candidates))

    except Exception as e:
        st.success("There is some issue in the application Contact the owner for the same")
        return None

if __name__ == "__main__":
    main()
