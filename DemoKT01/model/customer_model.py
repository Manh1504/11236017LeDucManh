class Customer:
    def __init__(self, customer_id, first_name, last_name, company, address, email):
        self.customer_id = customer_id
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.address = address
        self.email = email

    def to_dict(self):
        return self.__dict__
