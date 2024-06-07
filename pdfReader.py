import PyPDF2
import json

pdffileobj = open('AU127-1.pdf', 'rb')
pdfreader = PyPDF2.PdfFileReader(pdffileobj)
x = pdfreader.numPages

text = ""
for i in range(x):
    pageobj = pdfreader.getPage(i)
    pg = pageobj.extract_text()
    text += "\n"
    text += pg

with open("AU127-1.txt", "w") as file1:
    file1.write(text)

metadata = pdfreader.getDocumentInfo()
pdf_metadata = {
    "Author": metadata.author if metadata.author else 'Unknown',
    "Title": metadata.title if metadata.title else 'Unknown',
    "CreationDate": metadata['/CreationDate'] if '/CreationDate' in metadata else 'Unknown'
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
