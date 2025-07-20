from parser import extract_text
from extractor import extract_fields
from db import create_table, insert_data, fetch_all

# ✅ Set your receipt image path
image_path = r"C:\Users\Anju\OneDrive\Documents\esai\receipt_parser_project\data\receipt1.jpg"

# Step 1: OCR text
text = extract_text(image_path)
print("🔍 Extracted Text:\n", text)

# Step 2: Extract fields
fields = extract_fields(text)
print("\n📌 Extracted Fields:", fields)

# Step 3: Save to database
create_table()  # creates table if not exists
insert_data(fields["vendor"], fields["date"], fields["amount"])
print("\n✅ Data saved to database!")

# Step 4: Fetch and show saved receipts
all_receipts = fetch_all()
print("\n🧾 All saved receipts:")
for receipt in all_receipts:
    print(receipt)
