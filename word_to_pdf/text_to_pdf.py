'''Convert .txt file .pdf file'''

from fpdf import FPDF


def read_text_file(file_name):
    ''' Reading into .txt file '''

    with open(file_name, 'r', encoding='utf-8') as file:
        file_content = file.read()
        return file_content


def convert_text_to_pdf(file_content):
    ''' Function to convert .txt file contents to .pdf file '''

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font('Arial', size=14)
    pdf.multi_cell(w=0, h=10, txt=file_content, align='L')

    pdf.output('problem_solving.pdf')
