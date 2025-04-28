import re

def align_content(text):
    matches = re.findall(
        r'(\d+)\s+([A-Za-z\s]+)\s+([A-Za-z\s]+)\s+([A-Za-z\s]+)\s+(\d{2}/\d{2}/\d{4})\s+([A-Za-z]+)\s+([A-Z0-9]+)\s+([\d,]+\.\d+\$?)',
        text
    )
    
    if not matches:
        print("No structured rows found.")
        return []

    data = []
    for match in matches:
        data.append(match)

    return data
