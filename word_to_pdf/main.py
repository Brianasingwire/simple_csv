'''Main calling function'''

from text_to_pdf import read_text_file, convert_text_to_pdf


def main():
    '''

    Entry point for the text_to_pdf.py, this is brief exercise
    to convert .txt file to .pdf file

    '''

    file_name = 'problem_solving.txt'

    file_content = read_text_file(file_name)

    convert_text_to_pdf(file_content)


if __name__ == '__main__':
    main()
