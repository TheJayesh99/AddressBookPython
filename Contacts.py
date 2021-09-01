class Contact:
    def __init__(self,contact):
        self.first_name = contact.get("first_name")
        self.last_name = contact.get("last_name")
        self.address = contact.get("address")
        self.city = contact.get("city")
        self.state = contact.get("state")
        self.zip = contact.get("zip")
        self.phone_number = contact.get("phone_number")
        self.email = contact.get("email")
    
    def __str__(self) -> str:
        return f"First Name = {self.first_name} Last Name = {self.last_name} Address = {self.address} City = {self.city} State = {self.state} Zip = {self.zip} Phone Number = {self.phone_number} Email = {self.email}"