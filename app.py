# app.py – PolicyScan AI: Enterprise Compliance Validator with LLM

import streamlit as st
import fitz  # PyMuPDF
import docx2txt
import ollama
import json

# --- Extract Text ---
def extract_text(file):
    if file.name.endswith(".pdf"):
        with fitz.open(stream=file.read(), filetype="pdf") as doc:
            return "\n".join(page.get_text() for page in doc)
    elif file.name.endswith(".docx"):
        return docx2txt.process(file)
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    return ""

# --- AI Validator Agent Prompt ---
def generate_validator_prompt(text):
    prompt = f"""
You are an enterprise document compliance validator.

Scan the document below and perform:
1. Identify risky terms or phrases (e.g., 'no liability', 'at will', etc.)
2. Check for missing compliance keywords (e.g., 'GDPR', 'encryption', 'MFA')
3. Flag outdated language (e.g., 'fax', 'CD-ROM')
4. Provide a risk score between 0 and 100 (lower is riskier)
5. Suggest better alternatives or edits if possible

Respond in JSON format with:
- "risk_score": <int>
- "red_flags": ["..."]
- "missing_terms": ["..."]
- "suggestions": ["..."]

Document:
{text[:3000]}
"""
    return prompt

# --- LLM Query via Ollama ---
def query_llm(prompt):
    response = ollama.chat(model="llama3", messages=[{"role": "user", "content": prompt}])
    return response['message']['content']

# --- Streamlit UI ---
st.set_page_config(page_title="PolicyScan AI", layout="centered")
st.title("🔍 PolicyScan AI – Compliance Red Flag Scanner")
st.markdown("_Upload any policy or document to scan for risky language and missing compliance clauses._")

uploaded = st.file_uploader("Upload Policy Document (PDF, DOCX, TXT)", type=["pdf", "docx", "txt"])

if uploaded:
    with st.spinner("Scanning with Validator Agent..."):
        text = extract_text(uploaded)
        prompt = generate_validator_prompt(text)
        output_raw = query_llm(prompt)

        try:
            output = json.loads(output_raw)
        except:
            output = {}

    st.markdown("### 📊 Risk Score")
    st.metric("Risk Score", output.get("risk_score", "N/A"))

    st.markdown("### 🚩 Red Flags Detected")
    st.write(output.get("red_flags", []))

    st.markdown("### ⚠️ Missing Compliance Terms")
    st.write(output.get("missing_terms", []))

    st.markdown("### ✅ Suggestions & Fixes")
    st.write(output.get("suggestions", []))
else:
    st.info("Upload a policy document to begin scanning.")
