from src import get_data_from_pdf, align_content, extract_data

def main():
    pdf_path = "data/sample.pdf"
    output_path = "output/result.json"

    raw_text = get_data_from_pdf(pdf_path)
    aligned_content = align_content(raw_text)
    extracted_data = extract_data(aligned_content)

    print(f"Data saved to {output_path}")

if __name__ == '__main__':
    main()