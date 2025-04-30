# 🏥 Medical Helper

**Simplifying Medical Terminology for Everyone**

---

## 🧬 Project Overview

**Medical Helper** is a healthcare-focused AI tool developed during [**BioHacks 2025**](https://biohacks.devpost.com/), a beginner-friendly, bioinformatics-oriented hackathon hosted at UCSC. Our goal is to help patients better understand their diagnoses and treatment plans by translating complex medical language into clear summaries, along with research support from trusted databases.

---

## 🏆 Awards & Recognition

🎉 **Winner — Most Social Impact Award @ BioHacks 2025**  
🪙 *Prize: Amazon Fire 7 Tablet with accessories*

We were recognized for building a project that enhances accessibility and understanding in healthcare for underserved populations.

---

## 💡 What It Does

Medical Helper:
- 📄 Extracts text from PDF or TXT medical documents.
- ✂️ Summarizes medical content using AI language models.
- 🔎 Retrieves related research articles from PubMed.
- 🧠 (Optional) Explains medical terms in patient-friendly language using GPT-4.

---

## ⚙️ How It Works

- **Text Extraction**: Uses `pypdf` to read medical documents.
- **Summarization**: Uses Hugging Face’s `facebook/bart-large-cnn` model.
- **Research Support**: Accesses NCBI Entrez API to find PubMed articles.
- **AI Explanation**: (Optional) Uses OpenAI GPT-4 to explain diseases and treatments in layman's terms.

---

## 🛠️ Built With

- [Python](https://www.python.org/)
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [OpenAI API (GPT-4)](https://platform.openai.com/)
- [NCBI Entrez (BioPython)](https://biopython.org/)
- [PyPDF](https://pypi.org/project/pypdf/)

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- OpenAI API key set in the environment variable `OPENAI_API_KEY`
- Install dependencies:

```bash
pip install openai transformers biopython pypdf
