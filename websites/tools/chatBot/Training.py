import PyPDF2

def process_pdf(file_path):
    with open(file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
def training(List_file):
    list_text = []
    for file_path in List_file:
        text = process_pdf(file_path)
        list_text.append(text)
    text1 = list_text[0]
    text2 = list_text[1]
    text3 = list_text[2]
    text4 = list_text[3]
    return text1, text2, text3, text4

