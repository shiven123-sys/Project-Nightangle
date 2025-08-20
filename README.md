# Nightangle – AI Resume Screener

**Tagline:** *“Filtering the gold from the resumes, smarter and faster.”*

## Project Overview

Nightingale is an AI-powered Resume Screening system that helps recruiters quickly identify the most suitable candidates by analyzing resumes semantically. It goes beyond traditional keyword-based ATS systems by using advanced NLP techniques to understand the context of candidate experiences and skills.

## Features

* Upload resumes in **PDF** format.
* Extract text from resumes and perform **semantic search** using **Sentence Transformers**.
* Compare candidate skills with job descriptions to calculate **similarity scores**.
* Dashboard built with **Streamlit** to display candidate rankings, scores, and resume previews.
* Optionally link and verify candidates’ profiles from **GitHub** and **LinkedIn**.
* Detect potentially fake or misleading resumes (fraud detection module).
* Progress visualization while processing multiple resumes.

## Tech Stack

* **Backend:** Python, PyTorch, Sentence Transformers
* **Frontend:** Streamlit, HTML/CSS (for dashboard customization)
* **PDF Handling:** PyPDF2
* **Libraries:** Pandas, io, time, util (from sentence\_transformers)

## Installation

1. **Clone the repository:**

```bash
git clone <your-repo-link>
cd Nightangle
```

2. **Create a virtual environment (Linux example):**

```bash
python -m venv venv
source venv/bin/activate
```

3. **Install required packages:**

```bash
pip install -r requirements.txt
```

## Running the App

```bash
streamlit run app.py
```

## How It Works (Step by Step)

1. Upload a PDF resume.
2. The system extracts text from the PDF using PyPDF2.
3. Resume text is encoded into embeddings using a pretrained **MiniLM model**.
4. Compare candidate embeddings with the job description embedding to calculate similarity.
5. Display candidates in the dashboard with **similarity scores** and preview of their resume.
6. Optional GitHub/LinkedIn verification for authenticity.

## Future Enhancements

* Add multi-language support for resumes.
* Integrate an **interactive feedback system** for recruiters.
* Expand fraud detection using AI-powered anomaly detection.
* Deploy on **cloud services** for enterprise usage.

* Shivam Jain – Project Lead & Backend Developer
