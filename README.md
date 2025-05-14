# InvoiceAuditCrew - CrewAI Crew

## 🚀 Overview

InvoiceAuditCrew automates the extraction, categorization, and validation of data from uploaded invoices. It uses a team of AI agents to convert scanned or digital invoices into structured accounting-ready files, while also performing light auditing to detect duplicates, validate tax, and flag policy violations.

## ✨ Key Features

- **PDF Table Extractor (with OCR)**: Automatically extracts tabular data and metadata from scanned or digital invoice files using OCR and parsing logic.
- **Vendor & Currency Parser**: Identifies vendor names, invoice numbers, dates, and currencies, supporting multi-currency environments.
- **Line Item Categorizer**: Assigns appropriate accounting categories (e.g., Office Supplies, Software, Meals) to each invoice line item using AI-based classification.
- **Invoice Validator**: Performs auditing checks such as tax calculation verification, subtotal/total consistency, and date validation.
- **Duplicate Detector**: Flags potentially duplicated invoices based on fuzzy matching of invoice number, vendor, and amount.
- **Policy Compliance Auditor**: Cross-checks line items against a predefined set of company expense policies and flags violations.

## 🔍 Use Cases

This crew is ideal for:

- Freelancers and solopreneurs automating invoice bookkeeping.
- Small business owners reducing time spent on manual expense categorization.
- Accountants seeking to validate and summarize client expenses efficiently.

## 🛠️ Requirements

- CrewAI version: `>= 0.10.0`
- API Keys needed:
  - **OpenAI API**: For classification and language understanding tasks.

- OCR Requirement:
  - **Tesseract OCR** (Free & open-source):
    - No API key required — runs locally.
    - Installation:
      - Ubuntu: `sudo apt install tesseract-ocr`
      - macOS: `brew install tesseract`
      - Windows: [Download from GitHub](https://github.com/tesseract-ocr/tesseract)

- Additional dependencies:
  - `pytesseract`, `pdfplumber`, `pdf2image`, `pandas`, `openai`, `fuzzywuzzy`, `dateparser`

## 📊 Example Output

A clean CSV file or QuickBooks-compatible report like:

Date,Vendor,Item Description,Category,Amount,Currency,Audit_Flag
2025-05-01,Adobe Inc.,Photoshop Subscription,Software,29.99,USD,
2025-05-02,Staples,Office Chairs,Office Supplies,189.00,USD,
2025-05-03,Uber Eats,Team Lunch,Meals,120.00,USD,PolicyLimitExceeded
2025-05-04,Adobe Inc.,Photoshop Subscription,Software,29.99,USD,PossibleDuplicate


## 📚 Resources and References

- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [QuickBooks CSV Import Guide](https://quickbooks.intuit.com/learn-support/en-us/help-article/list-management/import-lists-in-quickbooks-online/L5sfm8Y3m_US_en_US)
- [CrewAI Framework](https://github.com/crewAIInc/crewAI)

## 🤝 Contributing

Have ideas for new validations or integrations? Fork the repo and submit a pull request! Contributions welcome.

## 📝 License

This project is released under the MIT License.

