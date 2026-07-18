from report import create_report
from gemini import generate_summary, compare_documents, calculate_similarity
from pdf_reader import extract_text_from_pdfs
import streamlit as st

# -------------------- Page Configuration --------------------
st.set_page_config(
    page_title="Multi-Document Comparison Tool",
    page_icon="📄",
    layout="wide"
)
# -------------------- Sidebar --------------------

with st.sidebar:

    st.title("🤖 AI Document Analyzer")

    st.markdown("---")

    st.subheader("👩‍💻 Developer")
    st.write("Anushka Soni")

    st.subheader("🎓 Project")
    st.write("IBM PBEL GenAI Final Project")

    st.subheader("🛠️ Tech Stack")

    st.write("🐍 Python")
    st.write("🎈 Streamlit")
    st.write("🤖 OpenRouter AI")
    st.write("📄 PDF Processing")

    st.markdown("---")

    st.success("🚀 Version 1.0")
    st.markdown("---")

    st.subheader("📊 Features")

    st.write("✅ Multi PDF Upload")
    st.write("✅ AI Summary")
    st.write("✅ Document Comparison")
    st.write("✅ Similarity Analysis")
    st.write("✅ PDF Report Download")

# -------------------- Session State --------------------
if "summary" not in st.session_state:
    st.session_state.summary = ""

if "comparison" not in st.session_state:
    st.session_state.comparison = ""

if "score" not in st.session_state:
    st.session_state.score = ""

# -------------------- UI --------------------
st.title("🤖 AI Multi-Document Comparison Tool")

st.caption("Upload multiple PDF files and let AI summarize, compare and analyze them.")

st.success("✅ IBM PBEL Final GenAI Project")

st.divider()

with st.expander("📌 How to Use", expanded=True):

    st.markdown("""
### Welcome 👋

Follow these simple steps:

1️⃣ Upload one or more PDF files.

2️⃣ Click **🚀 Analyze Documents**.

3️⃣ The AI will automatically generate:
- 📄 Summary
- 📊 Document Comparison
- 📈 Similarity Score

4️⃣ Click **📥 Download AI Report** to save the report as a PDF.
""")

uploaded_files = st.file_uploader(
    "Upload Multiple PDF Files",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:

    st.success(f"{len(uploaded_files)} PDF(s) uploaded successfully!")

    st.subheader("Uploaded Files")

    for file in uploaded_files:
        st.write(f"📄 {file.name}")

    text = extract_text_from_pdfs(uploaded_files)

    st.subheader("Preview of Extracted Text")
    st.text(text[:1500])

    st.divider()

    # -------------------- Analyze Documents --------------------

if st.button("🚀 Analyze Documents"):

    # Summary
    with st.spinner("Generating AI Summary..."):
        st.session_state.summary = generate_summary(text)

    st.subheader("📄 AI Summary")
    st.write(st.session_state.summary)

    st.divider()

    # Comparison
    with st.spinner("Comparing Documents..."):
        st.session_state.comparison = compare_documents(text)

    st.subheader("📊 Document Comparison")
    st.write(st.session_state.comparison)

    st.divider()

    # Similarity
    with st.spinner("Calculating Similarity..."):

        similarity = calculate_similarity(text)

        import re

        numbers = re.findall(r"\d+", similarity)

        if numbers:
            st.session_state.score = int(numbers[0])
        else:
            st.session_state.score = 0

    st.subheader("📈 Similarity Score")

    st.metric(
        "Similarity",
        f"{st.session_state.score}%"
    )

    st.progress(st.session_state.score / 100)

    if st.session_state.score >= 80:
        st.success("Excellent Match ✅")

    elif st.session_state.score >= 60:
        st.warning("Moderate Match ⚠️")

    else:
        st.error("Low Similarity ❌")

    st.divider()

    # Report
    report = create_report(
        st.session_state.summary,
        st.session_state.comparison,
        str(st.session_state.score)
    )

    with open(report, "rb") as file:

        st.download_button(
            label="📥 Download AI Report",
            data=file,
            file_name="AI_Report.pdf",
            mime="application/pdf"
        )
    st.success("🎉 Analysis Completed Successfully!")

    st.balloons()    

else:
    st.info("Please upload at least one PDF file.")