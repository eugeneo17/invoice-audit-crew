# 🧾 InvoiceAudit - CrewAI Crew


## 📘 Description

InvoiceAuditCrew is an AI-powered crew that automates the extraction, categorization, and auditing of invoice documents. Using OCR and language models, it processes PDF invoices into structured formats, identifies policy violations, flags duplicates, and ensures all invoices are audit-ready. This reduces manual bookkeeping efforts and improves financial accuracy and compliance.

## 💼 Example Use Cases

- **Freelancers and Consultants**  
  Automatically extract invoice data from scanned or emailed PDFs and generate categorized expense reports in seconds. Save hours each month otherwise spent on manual data entry, and ensure that income and expenses are ready for tax filing or client reimbursement.

- **Accountants Handling Large Volumes**  
  Upload dozens (or hundreds) of client invoices and let the system extract line items, apply accounting categories (e.g., Software, Meals, Travel), and run compliance checks (e.g., tax rate validation, missing vendor info). Bulk-export CSVs compatible with QuickBooks or Xero.

- **Small Business Owners Managing Vendor Payments**  
  Use the crew to catch duplicate or inflated charges across recurring invoices. For example, if a subscription charge appears twice with slightly different invoice numbers, the system will flag it. This prevents overpayments and improves accounts payable hygiene.

- **Finance & Operations Teams in Growing Startups**  
  Integrate this crew into your internal invoice intake pipeline. Automatically route suspicious invoices (e.g., wrong currency, mismatched totals) to a human reviewer while clean ones go straight to approval. Great for teams scaling up without adding extra accounting headcount.

- **Nonprofits & Grant-Funded Projects**  
  Generate audit-ready documentation for each invoice submitted to a grantor or funding agency. Quickly ensure all required fields (vendor name, date, description, currency) are present and properly categorized. Export a clean summary for reporting requirements.

- **Auditors & Internal Compliance Teams**  
  Run automated policy checks across invoice datasets to ensure purchases comply with internal spending rules (e.g., maximum per diem meal costs, allowed vendors, proper tax inclusion). Easily identify potential violations ahead of formal audits.


## 📦 Dependencies

- `crewai>=0.10.0`
- `pytesseract`
- `pdfplumber`
- `pdf2image`
- `pandas`
- `openai`
- `fuzzywuzzy`
- `dateparser`

**OCR Requirement**:
- Tesseract OCR (must be installed separately)
  - Ubuntu: `sudo apt install tesseract-ocr`
  - macOS: `brew install tesseract`
  - Windows: [Tesseract GitHub](https://github.com/tesseract-ocr/tesseract)

**API Keys Required**:
- OpenAI API

---

## ⚙️ Configuration Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-org/InvoiceAuditCrew.git
   cd InvoiceAuditCrew
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set OpenAI API Key**
   Create a `.env` file:
   ```env
   OPENAI_API_KEY=your-key-here
   ```

5. **Add invoice files**
   Place your test invoices in `input/invoice_sample.pdf` or replace with your own.

---

## 🚀 Usage Examples

### Run the full pipeline:
```bash
crewai run
```

### Train the crew:
```bash
crewai train --n_iterations 3 --filename training_results.pkl
```

### Test with different LLM models:
```bash
crewai test --n_iterations 2 --model gpt-4
```

---

## 🧾 Sample Output

### 📁 Output Directory: `output/`

- `invoice_summary_YYYYMMDD_HHMM.csv`: Categorized invoice lines with audit flags
- `audit_report_YYYYMMDD_HHMM.pdf`: Human-readable report of invoice findings


### 🧮 Example CSV:

A clean CSV file or QuickBooks-compatible report like:

```
Date,Vendor,Item Description,Amount,Currency,Category,Audit_Flag
2025-05-01,Adobe Inc.,Photoshop Subscription,29.99,USD,Software,
2025-05-03,Uber Eats,Team Lunch,120.00,USD,Meals,PolicyLimitExceeded
2025-05-04,Adobe Inc.,Photoshop Subscription,29.99,USD,Software,PossibleDuplicate
```
### 🧮 Output Example PDF

Below is a sample of the generated **Audit Report PDF**, which summarizes issues identified in each invoice in a human-readable format:

---

**Audit Report – Generated: 2025-05-01**

**Invoice from: Adobe Inc.**  
**Invoice Date:** 2025-05-01  
**Item Description:** Photoshop Subscription  
**Amount:** 29.99 USD  
**Category:** Software

**Audit Results:**
- ✅ No issues detected

---

**Invoice from: Uber Eats**  
**Invoice Date:** 2025-05-03  
**Item Description:** Team Lunch  
**Amount:** 120.00 USD  
**Category:** Meals

**Audit Results:**
- ❗ Policy Violation: Lunch expense exceeded allowed limit (PolicyLimitExceeded)

---

**Invoice from: Adobe Inc.**  
**Invoice Date:** 2025-05-04  
**Item Description:** Photoshop Subscription  
**Amount:** 29.99 USD  
**Category:** Software

**Audit Results:**
- ⚠️ Duplicate Detected: Similar invoice already exists

---

📁 This PDF is saved to: `output/audit_report_YYYYMMDD_HHMM.pdf`

## 📚 References

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [CrewAI Framework](https://github.com/crewAIInc/crewAI)
- [QuickBooks CSV Guide](https://quickbooks.intuit.com/learn-support/en-us/help-article/list-management/import-lists-in-quickbooks-online/L5sfm8Y3m_US_en_US)

## 🤝 Contributing

Contributions are welcome! Whether it's new audit rules, integrations, or UI hooks, feel free to fork and submit a pull request.

---

## 📄 License

Licensed under the MIT License.

