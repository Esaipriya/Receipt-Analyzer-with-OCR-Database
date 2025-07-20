import streamlit as st
import os
from parser import extract_text
from extractor import extract_fields
from db import create_table, insert_data, fetch_all

# ✅ NEW: Import your algorithms
from algorithms import to_dataframe, aggregate_stats, group_by_vendor, time_series

# Set page title and layout
st.set_page_config(page_title="🧾 Receipt Analyzer", layout="centered")
st.title("🧾 Receipt Analyzer with OCR + Database")

# Step 1: Ensure the DB table exists
create_table()

# Step 2: File Upload
uploaded_file = st.file_uploader("Upload a Receipt (.jpg, .png, .pdf)", type=["jpg", "png", "pdf"])

if uploaded_file:
    # Save file locally
    save_dir = "uploaded_receipts"
    os.makedirs(save_dir, exist_ok=True)
    file_path = os.path.join(save_dir, uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("✅ File uploaded successfully!")

    # Step 3: Extract Text via OCR
    text = extract_text(file_path)
    st.subheader("📄 Extracted Text:")
    st.text_area("Raw OCR Text", text, height=200)

    # Step 4: Extract Vendor, Date, Amount
    fields = extract_fields(text)
    st.subheader("📌 Extracted Fields:")
    st.json(fields)

    # Step 5: Save to database
    insert_data(fields["vendor"], fields["date"], fields["amount"])
    st.success("✅ Data saved to SQLite database!")

# Step 6: Show Table of All Receipts
st.markdown("---")
st.header("📋 All Saved Receipts")
records = fetch_all()

if records:
    # ✅ Use your algorithm functions
    df = to_dataframe(records)
    st.dataframe(df)

    # ✅ Summary Stats using algorithm
    st.header("📊 Summary")
    stats = aggregate_stats(df)
    st.write("🧾 Total Spend:", round(stats["Total Spend"], 2))
    st.write("💰 Average Spend:", round(stats["Average"], 2))
    st.write("🏆 Top Vendor:", stats["Top Vendor"])

    # ✅ Bar Chart - Spend per Vendor
    st.subheader("💸 Spend per Vendor")
    vendor_data = group_by_vendor(df)
    st.bar_chart(vendor_data.set_index("Vendor"))

    # ✅ Line Chart - Monthly Spend Trend
    st.subheader("📅 Monthly Spending Trend")
    ts_data = time_series(df)
    if not ts_data.empty:
        ts_data["Date"] = ts_data["Date"].astype(str)  # convert Period to string for plotting
        st.line_chart(ts_data.set_index("Date"))
    else:
        st.info("Not enough data to show time-series trend.")

else:
    st.warning("No receipts saved yet.")
