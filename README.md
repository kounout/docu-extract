# DocuExtract

An interactive web application built with Python and Streamlit that uses Google Gemini to automatically parse and extract structured data from invoices and uploaded PDF documents.

## Why I Built This

Manually processing invoices, reading through multi-page documents, and typing out line items is tedious and prone to human error. I built this app as part of my Erasmus+ portfolio to automate invoice data extraction, turning unstructured documents into clean, structured tabular data quickly and efficiently.

## Core Features

- **Document Upload:** Seamlessly upload `.pdf` invoices directly through a clean Streamlit interface.
- **Intelligent Extraction:** Powered by Google Gemini (`gemini-3.8-flash`) to accurately identify and extract key invoice fields, totals, and metadata.
- **Structured Data Display:** Organizes parsed information dynamically using Pandas dataframes.
- **Secure API Integration:** Manages API credentials using environment variables (`.env`) to keep secret keys safe and private.

## Tech Stack

- **Interface:** Streamlit
- **AI/LLM:** Google Gemini API (`google-genai` SDK)
- **Data Processing:** pandas
- **PDF Extraction:** pypdf
- **Environment Management:** python-dotenv

## Getting Started

### Prerequisites

- Python 3.10+ installed on your system.
- A Gemini API key from [Google AI Studio](https://aistudio.google.com/).

### Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/kounout/docu-extract.git](https://github.com/kounout/docu-extract.git)
   cd docu-extract
