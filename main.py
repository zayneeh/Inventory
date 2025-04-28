from scripts.Extract_data import get_data_from_pdf
from scripts.Load_in_json import extract_data
from scripts.Align import align_content
import json

def main():
    pdf_path = "data\home_inventory.pdf"
    output_path = r"data\result.json"

    raw_text = get_data_from_pdf(pdf_path)
    aligned_contents = align_content(raw_text)
    extracted_data = extract_data(raw_text, aligned_contents)

    #Save to JSON file
    with open(output_path, "w") as f:
        json.dump(extracted_data, f)

    print(f"Data saved to {output_path}")

if __name__ == '__main__':
    main()