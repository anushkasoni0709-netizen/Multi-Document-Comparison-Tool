from pypdf import PdfReader

def extract_text_from_pdfs(uploaded_files):
    """
    Extract text from multiple uploaded PDF files.
    """

    all_text = ""

    for pdf in uploaded_files:
        reader = PdfReader(pdf)

        for page in reader.pages:
            text = page.extract_text()

            if text:
                all_text += text + "\n"

    return all_text