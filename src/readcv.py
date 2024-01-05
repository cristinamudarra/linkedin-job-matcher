import PyPDF2

def get_pdf(file_path):
    all_text = ""

    # Abrir el archivo en modo lectura binaria
    with open(file_path, 'rb') as file:
        # Crear un objeto de lectura PDF
        pdf_reader = PyPDF2.PdfReader(file)

        # Obtener el número de páginas del PDF
        num_pages = len(pdf_reader.pages)

        # Leer cada página del PDF
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text = page.extract_text()

            # Agregar el texto de la página actual a la lista
            all_text += text
    
    return all_text