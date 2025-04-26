import json 


def align_data():
    #aligns them line by line as it appears in the PDF.
    lines = raw_text.split('\n')
    aligned = [line.strip() for line in lines if line.strip()]
    return aligned

def extract_data():

    #extracted into a dictionary 

    #Process date 

    # Save to JSON file
    with open(output_path, "w") as f:
        json.dump(extracted_data, f)

    return data