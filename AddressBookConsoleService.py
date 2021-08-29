from Contacts import Contact

class AddressBookConsoleService:
    def createContact(self):
        contact_dict = {
            "first_name" : "Jayesh",
            "last_name" : "Mali",
            "address" : "kharghar",
            "city" : "Mumbai",
            "state" : "Maharashtra",
            "zip" : "410210",
            "number" : "number",
            "email" : "jay@mail.com"
        }
        contact = Contact(contact_dict)
        print("Contact created ")
        return contact
        
    def displayContact(self,contact):
        print(contact)
