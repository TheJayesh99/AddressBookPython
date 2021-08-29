from Contacts import Contact

class AddressBookConsoleService:
    contact_list = []
    def create_contact(self):
        first_name = input("Enter first name \n")
        last_name = input("Enter last name \n")
        address = input("Enter address \n")
        city  = input("Enter city \n")
        state = input("Enter state \n")
        zip  = input("Enter zip code \n")
        phone_number = input("Enter phone number \n")
        email = input("Enter email address \n")
        contact_dict = {
            "first_name" : first_name,
            "last_name" : last_name,
            "address" : address,
            "city" : city,
            "state" : state,
            "zip" : zip,
            "number" : phone_number,
            "email" : email
        }
        contact = Contact(contact_dict)
        return contact

    def add_contact(self):
        contact = self.create_contact()
        self.contact_list.append(contact)

    def display_contact(self):
        contacts = "\n".join(str(contact) for contact in self.contact_list ) 
        print(contacts)
