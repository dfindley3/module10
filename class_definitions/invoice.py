#!/usr/local/bin/python3

class Invoice:
    def __init__(self, id, cid, lname, fname, pnumber, addy, items=None):
        self.invoice_id = id
        self.customer_id = cid
        self.last_name = lname
        self.first_name = fname
        self.phone_number = pnumber
        self.addy = addy
        self.items_with_price = items

    def set_invoice_id(self, id):
        self.set_invoice_id = id

    def set_customer_id(self, cid):
        self.set_customer_id = cid
    
    def set_last_name(self, lname):
        self.last_name = lname

    def set_first_name(self, fname):
        self.first_name = fname

    def set_phone_number(self, pnumber):
        self.phone_number = pnumber
    
    def set_addy(self, addy):
        self.addy = addy
    
    def set_items(self, items):
        self.items_with_price = items

    def __str__(self):
        return self.customer_id + ":" + self.last_name + "," + self.first_name + ";" + "Phone:" + "" + self.phone_number
    
    def __repr__(self):
        return 'Customer({},{},{},{},{})'.format(self.customer_id, self.last_name, self.first_name, self.invoice_id, self.phone_number, self.addy, self.items_with_price)

    def add_item(self, items):
        self.items_with_price.update(items)

    def create_invoice(self):
        if (self.items_with_price == None):
            raise ValueError("Nothing in items_with_price")
        subtotal = 0.0
        total = 0.0
        for key, value in self.items_with_price.items():
            subtotal += value
        tax = float(subtotal * 0.08)
        total = subtotal + tax

        for key, value in self.items_with_price.items():
            print("{0} ..... ${1:.2f}".format(key, value))
            print("Tax ..... ${0:.2f}".format(tax))
            print("Total ..... ${0:.2f}".format(total))

customer_one = Invoice("1046", "123-453", "Cook", "Tim", "515-555-1234", "5050 3rd street", {"iPad" : 499.99})
print(str(customer_one))
customer_one.add_item({"MacBook" : 599.99})
customer_one.create_invoice()
del customer_one