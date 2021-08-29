from Contacts import Contact

class AddressBookConsoleService:
    
    contact_list = []

    def create_contact(self):
        
        """
        Method to create contact object
        """
        contact_dict = {
            "first_name" : "",
            "last_name" : "",
            "address" : "",
            "city" : "",
            "state" : "",
            "zip" : "",
            "number" : "",
            "email" : ""
        }
        contact = Contact(contact_dict)
        contact = self.get_Details(contact)
        return contact

    def get_Details(self,contact):

        """
        Method to fetch contact details from user
        """
        contact.first_name = input("Enter first name \n")
        contact.last_name = input("Enter last name \n")
        contact.address = input("Enter address \n")
        contact.city  = input("Enter city \n")
        contact.state = input("Enter state \n")
        contact.zip  = input("Enter zip code \n")
        contact.phone_number = input("Enter phone number \n")
        contact.email = input("Enter email address \n")
        return contact

    def add_contact(self):

        """
        Method to add contact to local storage
        """
        contact = self.create_contact()
        self.contact_list.append(contact)

    def display_contact(self):

        """
        Method to display all the contact that are present in the local storage
        """
        contacts = "\n".join(str(contact) for contact in self.contact_list ) 
        print(contacts)

    def edit_contact(self):
        
        """
        Method to edit existing contact
        """
        first_name = input("Enter the person name of whom contact you have to edit \n")
        contact_to_edit = [contact for contact in self.contact_list if contact.first_name == first_name] 
        if len(contact_to_edit) == 0:
            print("Contact not found")
        else: 
            self.get_Details(contact_to_edit[0])
            print("Contact Edited Sucessfully")