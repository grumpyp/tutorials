from pypdf import PdfReader


def load_pdf(file_path: str):
    reader = PdfReader(file_path)
    number_of_pages = len(reader.pages)

    with open ("result.txt", "w") as f:
        for i in range(number_of_pages):
            page = reader.pages[i]
            text = page.extract_text().strip()
            f.write(text.replace("\n", " "))

        f.close()