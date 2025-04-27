import re

def align_data(raw_text):
    lines = raw_text.split('\n')
    aligned = []
    buffer = ""

    for line in lines:
        line = line.strip()
        if not line:
            continue

        if re.match(r'^\d+', line):  
            if buffer:
                aligned.append(buffer.strip())
            buffer = line
        else:
            buffer += ' ' + line  

    if buffer:
        aligned.append(buffer.strip())

    return aligned
