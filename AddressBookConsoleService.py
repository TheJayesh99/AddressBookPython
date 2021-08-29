from Contacts import Contact

class AddressBookConsoleService:
    def createContact(self):
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
        
    def displayContact(self,contact):
        print(contact)
