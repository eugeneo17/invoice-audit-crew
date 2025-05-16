from crewai.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type
from pdf2image import convert_from_path
from pytesseract import image_to_string
from PIL import Image
import os
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

class ExtractTextInput(BaseModel):
    invoice_path: str = Field(..., description="Full path to the invoice file (PDF, PNG, JPG)")

class ExtractTextFromInvoiceTool(BaseTool):
    name: str = "Extract Invoice Text Tool"
    description: str = "Extracts text from an invoice file using OCR. Supports PDF, JPG, PNG."
    args_schema: Type[BaseModel] = ExtractTextInput

    def _run(self, invoice_path: str) -> str:
        print(f"[DEBUG] ExtractTextFromInvoiceTool running on: {invoice_path}")
        ext = os.path.splitext(invoice_path)[-1].lower()

        try:
            if ext in [".jpg", ".jpeg", ".png"]:
                img = Image.open(invoice_path)
                return image_to_string(img)

            elif ext == ".pdf":
                images = convert_from_path(invoice_path)
                text = ""
                for page in images:
                    text += image_to_string(page)
                return text

            else:
                return f"Unsupported file type for OCR: {ext}"

        except Exception as e:
            return f"OCR extraction failed: {str(e)}"

class SaveReportInput(BaseModel):
    csv_content: str
    pdf_content: str

class SaveReportTool(BaseTool):
    name: str = "Save Report Tool"
    description: str = "Saves invoice audit summary and PDF report to output files"
    args_schema: Type[BaseModel] = SaveReportInput

    def _run(self, csv_content: str, pdf_content: str) -> str:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M')
        print(f"[DEBUG] SaveReportTool called with timestamp={timestamp}")

        try:
            output_dir = os.path.abspath("output")
            os.makedirs(output_dir, exist_ok=True)

            csv_path = os.path.join(output_dir, f"invoice_summary_{timestamp}.csv")
            pdf_path = os.path.join(output_dir, f"audit_report_{timestamp}.pdf")

            with open(csv_path, "w") as f:
                f.write(csv_content)

            # Generate real PDF
            c = canvas.Canvas(pdf_path, pagesize=letter)
            width, height = letter
            y = height - 40
            for line in pdf_content.splitlines():
                c.drawString(40, y, line)
                y -= 14
                if y < 40:
                    c.showPage()
                    y = height - 40
            c.save()

            return f"Saved CSV to {csv_path} and PDF to {pdf_path}"
        except Exception as e:
            return f"[ERROR] Failed to write files: {e}"
