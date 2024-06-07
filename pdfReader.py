import PyPDF2
import json

pdffileobj = open('AU127-1.pdf', 'rb')
pdfreader = PyPDF2.PdfReader(pdffileobj)
x = len(pdfreader.pages)

text = ""
for i in range(x):
    pageobj = pdfreader.pages[i]
    pg = pageobj.extract_text()
    text += "\n"
    text += pg

with open(r"AU127-1.txt", "w") as file1:
    file1.writelines(text)

metadata = pdfreader.metadata
pdf_metadata = {
    "Author": metadata.get('/Author', 'Unknown'),
    "Title": metadata.get('/Title', 'Unknown'),
    "CreationDate": metadata.get('/CreationDate', 'Unknown')
}

data = {
    "Metadata": pdf_metadata,
    "Content": text
}

with open("text.json", 'w') as f:
    json.dump(data, f, indent=4)

print("PDF Metadata:")
print(json.dumps(pdf_metadata, indent=4))

pdffileobj.close()

file1 = open(r"AU127-1.txt", "a")
file1.writelines(text)
json_data = json.dumps(data)

f = open("text.json", 'w')
f.write(json_data)
f.close()

json = json.dump(file1)

f = open("text.json", 'w')
f.write(json)
f.close()
