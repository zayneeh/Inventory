class OwnerInfo:
    def __init__(self, owner_name, owner_address, owner_telephone):
        self.owner_name = owner_name
        self.owner_address = owner_address
        self.owner_telephone = owner_telephone

class Inventory:
    def __init__(self, purchase_date, serial_number, description, source, style, area, value):
        self.purchase_date = purchase_date
        self.serial_number = serial_number
        self.description = description
        self.source = source
        self.style = style
        self.area = area
        self.value = value
