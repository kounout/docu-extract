import os
import streamlit as st
import pandas as pd
from pypdf import PdfReader
from dotenv import load_dotenv
from google import genai


load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

st.title("🧾 DocuExtract: Invoice Parser")
st.write("Upload a PDF invoice to extract structured data.")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file is not None:
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""

    if st.button("Extract Data"):
        with st.spinner("Analyzing document..."):
            prompt = f"Extract Vendor, Date, Invoice #, and Total Amount from this text:\n\n{text}"

            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=prompt
            )

            st.subheader("Extracted Details:")
            st.write(response.text)

            df = pd.DataFrame({"Extracted Summary": [response.text]})
            csv_data = df.to_csv(index=False).encode('utf-8')

            st.download_button(
                label="Download as CSV",
                data=csv_data,
                file_name="invoice_summary.csv",
                mime="text/csv"
            )
