import json
import re  
from datetime import datetime
from .Classes import OwnerInfo, Inventory

# Format of the json data 
def json_response(owner_info, inventory_list):
    response = {
        "owner_name": owner_info.owner_name,
        "owner_address": owner_info.owner_address,
        "owner_telephone": owner_info.owner_telephone,
        "data": []
    }

    for item in inventory_list:
        response["data"].append({
            "purchase_date": item.purchase_date,
            "serial_number": item.serial_number,
            "description": item.description,
            "source": item.source,
            "style": item.style,
            "area": item.area,
            "value": item.value
        })

    return response


# Function Using regex to extract owner info
def extract_owner_info(raw_text):
    name_pattern = r"Owner Information\s*\n(.*?)\n"
    address_pattern = r"Owner Information\s*\n.*?\n(.*?)\n"
    phone_pattern = r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}"


    name_match = re.search(name_pattern, raw_text, re.DOTALL)
    address_match = re.search(address_pattern, raw_text, re.DOTALL)
    phone_match = re.search(phone_pattern, raw_text)

    owner_name = name_match.group(1).strip() if name_match else None
    owner_address = address_match.group(1).strip() if address_match else None
    owner_phone = phone_match.group(0).strip() if phone_match else None

    return owner_name, owner_address, owner_phone

#Function to Extract data from raw text
def extract_data(raw_text, aligned_rows):
    inventories = []

    owner_name, owner_address, owner_phone = extract_owner_info(raw_text)
    owner_info = OwnerInfo(owner_name, owner_address, owner_phone)

    for parts in aligned_rows:
        if len(parts) == 8:
            try:
                _, area, item_description, source, purchase_date_raw, style, serial_number, value_raw = parts

                # Parse date
                try:
                    purchase_date = datetime.strptime(purchase_date_raw, "%d/%m/%Y").isoformat()
                except ValueError:
                    try:
                        purchase_date = datetime.strptime(purchase_date_raw, "%d/%m/%y").isoformat()
                    except ValueError:
                        purchase_date = None

                value = value_raw.replace("$", "").replace(",", "").strip()

                # Pass Inventory daata
                item = Inventory(
                    purchase_date=purchase_date,
                    serial_number=serial_number.strip(),
                    description=item_description.strip(),
                    source=source.strip(),
                    style=style.strip(),
                    area=area.strip(),
                    value=value
                )
                inventories.append(item)
            except Exception as e:
                print(f"Failed to process row: {parts}")
                print(f"Reason: {str(e)}")
                continue

    return json_response(owner_info, inventories)
