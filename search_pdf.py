from pypdf import PdfReader
import re
import json
reader = PdfReader("CEAs/KiwiBank CA 2025-26.pdf")
doc = []
for i in range(len(reader.pages)):
    page = reader.pages[i]
    # print(page)
    # if "NEW EMPLOYEES" in page.extract_text():
    lines = page.extract_text().split('\n')
    doc.extend(lines)
    # print(page.extract_text().split('\n'))
    # print(page.extract_text()) 

doc = list(filter(lambda x: x.strip() != '', doc))

indexes = [i for i, line in enumerate(doc) if re.search(r'^\d+\.\d+', line)]
# print(doc)  
with open("indexes.json", "w") as file:
    json.dump(indexes, file, indent=2)
with open("output.json", "w") as file:
    json.dump(doc, file, indent=2)

ca_json = {}

for ci in range(len(indexes)):
    clause_index = indexes[ci]
    next_clause_index = indexes[ci + 1] if ci + 1 < len(indexes) else len(doc)
    clause_lines = doc[clause_index:next_clause_index]
    
    # Extract clause number (e.g., 6.3) from the first line
    match = re.match(r'^(\d+\.\d+)\s*(.*)', clause_lines[0].strip())
    if match:
        clause_number = match.group(1)
        first_line_content = match.group(2)
    else:
        clause_number = clause_lines[0].strip()
        first_line_content = ""

    # Combine first line content with the rest of the clause
    clause_content = "\n".join([first_line_content] + clause_lines[1:]).strip()
    ca_json[clause_number] = clause_content

with open("ca.json", "w") as file:
    json.dump(ca_json, file, indent=2)
