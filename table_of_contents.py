# from pypdf import PdfReader
# reader = PdfReader("CEAs/Department-of-Internal-Affairs-signed-CA-190724-to-310326.pdf")
# for i in range(len(reader.pages)):
#     page = reader.pages[i]
#     if "6.5" in page.extract_text():
#         print(page.extract_text())   \
import pdfplumber
import re

# Path to your PDF file
pdf_path = "CEAs/KiwiBank CA 2025-26.pdf"

# Regex pattern to match clause headers (e.g., "Clause 1: Title" or "1. Title")
clause_pattern = re.compile(r'(Clause\s+\d+[:.]?\s+.+)|(^\d+\.\s+.+)')

with pdfplumber.open(pdf_path) as pdf:
    for page_num, page in enumerate(pdf.pages, start=1):
        text = page.extract_text()
        if not text:
            continue
        for line in text.split('\n'):
            match = clause_pattern.match(line.strip())
            if match:
                print(match.group().strip())
