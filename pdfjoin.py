import PyPDF2
from sys import argv


def merge_files(files, output):

    # Define an empty list to hold all the PDFs
    pdfs_to_merge = []

    # Loop through your PDF files and add them to the list
    for file in files:
        pdfs_to_merge.append(open(file, 'rb'))

    # Create a new PDF writer object
    writer = PyPDF2.PdfWriter()

    # Loop through each PDF in the list and add its pages to the new PDF
    for pdf in pdfs_to_merge:
        pdf_reader = PyPDF2.PdfReader(pdf)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            writer.add_page(page)

    # Write the merged PDF to a new file
    with open(output, 'wb') as output_file:
        writer.write(output_file)

    # Close all the opened PDF files
    for pdf in pdfs_to_merge:
        pdf.close()


def get_files(file_list):
    files = []

    with open(file_list, 'r') as file_list:
            files = [line.strip() for line in file_list.readlines()]

    return files


def merge(file_list, output):
    files = get_files(file_list)
    merge_files(files, output)


if __name__ == '__main__':
    if len(argv) != 3:
        print('USAGE: ./python pdfjoin.py <INPUT FILE LIST> <OUTPUT FILE>')
    else:
        merge(argv[1], argv[2])
