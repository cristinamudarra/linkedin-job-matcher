import PyPDF2


def get_pdf(file_path):
    all_text = ""

    pdf_reader = PyPDF2.PdfReader(file_path)

    num_pages = len(pdf_reader.pages)
    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        text = page.extract_text()

        all_text += text

    return all_text
