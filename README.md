# JU14-PolicyScan-AI
GEN AI

🔍 PolicyScan AI – Enterprise Document Scanner for Red Flags & Compliance Violations
📄 What It Does
PolicyScan AI scans any uploaded document (e.g., internal policies, guidelines, contracts) and uses an AI Validator Agent to:

Detect risky language (e.g., “at will”, “unauthorized access”, “no liability”)

Flag missing compliance keywords (e.g., “GDPR”, “data encryption”, “access control”)

Summarize violations in simple terms

Suggest edits or replacements

Rate document compliance score from 0 to 100

🔐 Use Cases
| 🧠 HR Policies | Detect outdated language or missing diversity clauses |
| ⚖️ Legal Docs | Flag clauses that pose liability |
| 🔒 Security SOPs | Find missing data protection, MFA, or audit logs keywords |

🧠 Validator Agent Logic
Step 1: Extract text from PDF/DOCX

Step 2: Run AI agent to scan text using prompt like:

"Find risky phrases, missing compliance-related terms, or outdated policy language"

Step 3: Return:

Red flags

Missing elements

Suggested changes

Risk score (0-100)

📘 README.md
markdown
Copy
Edit
# 🔍 PolicyScan AI – Enterprise Compliance Red Flag Scanner

Scan any internal policy, SOP, HR guideline, or legal document to find risky phrases, outdated terms, and missing compliance clauses using LLMs.

---

## ✅ Features

- Upload DOCX, PDF, or TXT
- AI Validator Agent flags:
  - 🔴 Risky phrases (e.g., “no liability”, “at will”)
  - ❌ Missing terms (e.g., “GDPR”, “encryption”, “MFA”)
  - 🕰 Outdated language (e.g., “fax”, “CD-ROM”)
- 📊 Risk score (0 = risky, 100 = safe)
- ✅ Natural language suggestions for improvement

---

## 🧪 Sample Output

```json
{
  "risk_score": 62,
  "red_flags": ["'at will employment' lacks legal backing", "'no responsibility for data loss'"],
  "missing_terms": ["GDPR", "encryption", "2FA"],
  "suggestions": ["Replace 'no responsibility' with 'limited liability under GDPR clause XYZ'"]
}
🚀 Run Locally
bash
Copy
Edit
git clone https://github.com/yourusername/policyscan-ai.git
cd policyscan-ai
pip install -r requirements.txt
ollama pull llama3
streamlit run app.py
🔮 Future Features
Inline diff highlighter (HTML)

Export PDF compliance report

Upload 2 docs and compare versions

yaml
Copy
Edit

---

Would you like to:
- 📤 Add export to PDF?
- 🔎 Include visual highlights in text?
- 🧠 Connect to external compliance APIs?

Let me know and I’ll build it for you!
