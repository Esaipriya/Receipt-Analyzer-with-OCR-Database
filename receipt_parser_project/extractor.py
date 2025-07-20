import re

def extract_fields(text):
    
    lines = [line.strip() for line in text.split("\n") if line.strip()]
    vendor = lines[0] if lines else "Unknown"
    date = re.findall(r'\b(?:\d{1,2}[/-])?\d{1,2}[/-]\d{2,4}\b', text)
    amount = re.findall(r'(?:Total|Amount)[^\d]*([\d,]+\.\d{2})', text)

    return {
    "vendor": vendor,
    "date": date[0] if date else "Unknown",
    "amount": amount[-1].replace(",", "") if amount else "0.0"
    }

