import pdfplumber

# Extract Project Roadmap
print("=" * 80)
print("PROJECT ROADMAP")
print("=" * 80)
with pdfplumber.open('ironhack roadmap - Project Roadmap.pdf') as pdf:
    for i, page in enumerate(pdf.pages):
        text = page.extract_text()
        if text:
            print(f"\n--- Page {i+1} ---\n{text}")

print("\n\n")

# Extract Competitors Analysis
print("=" * 80)
print("COMPETITORS ANALYSIS")
print("=" * 80)
with pdfplumber.open('ironhack roadmap - Competitors Analysis.pdf') as pdf:
    for i, page in enumerate(pdf.pages):
        text = page.extract_text()
        if text:
            print(f"\n--- Page {i+1} ---\n{text}")
