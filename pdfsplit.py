import PyPDF2
import sys


def extract_pages(input_filename, pages_to_extract, output_filename):
    """
    Extracts a subset of pages from a PDF and saves them to a new PDF.

    Args:
      input_filename: Path to the existing PDF document.
      pages_to_extract: A list containing the page numbers (0-based indexing)
                        of the pages to extract.
      output_filename: Path to save the new PDF document with the extracted pages.
    """
    with open(input_filename, 'rb') as input_file, open(output_filename, 'wb') as output_file:
        pdf_reader = PyPDF2.PdfReader(input_file)
        pdf_writer = PyPDF2.PdfWriter()

        # Extract and add specified pages
        for page_num in pages_to_extract:
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

        pdf_writer.write(output_file)


def split(input, pages, output):
        extract_pages(input, [int(page_number) - 1 for page_number in pages.split(',')], output)
        print(f"Extracted pages {pages} from '{input}' and saved to '{output}'.")


if __name__ == '__main__':
    if len(sys.argv) !=4:
        print('USAGE: python pdfsplit.py <input> <page numbers separated by commas> <output>')
    else:
        split(sys.argv[1], sys.argv[2], sys.argv[3])
