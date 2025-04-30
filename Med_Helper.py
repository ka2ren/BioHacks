from openai import OpenAI
from transformers import pipeline
from Bio import Entrez
from pypdf import PdfReader
import os 
import openai

api_key = os.getenv("OPENAI_API_KEY")

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    with open(pdf_path, "rb") as file:
        reader = PdfReader(file)
        text = "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])
    return text

def summarize_text(text):
    """Summarize medical text using Hugging Face transformers."""
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    return summarizer(text, max_length=500, min_length=50, do_sample=False)[0]['summary_text']

def search_pubmed(query):
    """Retrieve relevant research from PubMed."""
    Entrez.email = "jaynaschick@gmail.com"
    handle = Entrez.esearch(db="pubmed", term=query, retmax=5)
    record = Entrez.read(handle)
    return [f"https://pubmed.ncbi.nlm.nih.gov/{id_}/" for id_ in record["IdList"]]

def explain_disease_and_treatment(disease):
    """Use OpenAI to provide a detailed explanation of a disease and its treatment."""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "Provide a detailed explanation of diseases and their treatments in an easy-to-understand way."},
                  {"role": "user", "content": f"Explain the disease {disease} in detail and list its treatment options."}]
    )
    return response["choices"][0]["message"]["content"]

def main():
    choice = input("Enter '1' to upload a medical text file (PDF or TXT) or '2' to enter a diagnosis: ")

    if choice == '1':
        file_path = input("Enter the file path: ")
        if file_path.endswith(".pdf"):
            text = extract_text_from_pdf(file_path)
        elif file_path.endswith(".txt"):
            with open(file_path, "r", encoding="utf-8") as file:
                text = file.read()
        else:
            print("Unsupported file format.")
            return

        print("\nSummarizing text...")
        summary = summarize_text(text)
        print("Summary:", summary)

        print("\nSearching for related research on PubMed...")
        pubmed_links = search_pubmed(text)
        print("Relevant research:")
        for link in pubmed_links:
            print(link)

    elif choice == '2':
        disease = input("Enter the medical diagnosis: ")
        print("\nSearching for related research on PubMed...")
        pubmed_links = search_pubmed(disease)
        print("Relevant research:")
        for link in pubmed_links:
            print(link)
        
        print("\nSummarizing text...")
        summary = summarize_text(disease)
        print("Summary:", summary)

       
        #print("\nRetrieving detailed explanation...")
        #explanation = explain_disease_and_treatment(disease)
        #print("Explanation:", explanation)
    
    else:
        print("Invalid choice.")
        return

if __name__ == "__main__":
    main()
