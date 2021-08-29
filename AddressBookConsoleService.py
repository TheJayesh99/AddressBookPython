from Contacts import Contact

class AddressBookConsoleService:
    
    address_books = {}

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
        print("contact created")
        address_book_name = input("Enter the address book name \n")
        address_book = self.address_books.get(address_book_name) 
        # if book does no already exists then creating a new book
        if address_book == None:
            contact_list = [contact]
            self.address_books[address_book_name] = contact_list
        # if book already exsists then adding contact to existing book   
        else:
            address_book.append(contact)

    def display_contact(self):

        """
        Method to display all the contact that are present in the local storage
        """
        for address_book in self.address_books:
            contacts = "\n".join(str(contact) for contact in self.address_books.get(address_book)) 
            print(f"Contacts In {address_book} are \n{contacts}")

    def edit_contact(self):
        
        """
        Method to edit existing contact
        """
        book_name = input("Enter the address book name ")
        address_book = self.address_books.get(book_name)
        if address_book != None:
            first_name = input("Enter the person name \n")
            contact_to_edit = [contact for contact in address_book if contact.first_name == first_name]
            if len(contact_to_edit) == 0:
                print("Contact not found")
            else: 
                self.get_Details(contact_to_edit[0])
                print("Contact Edited Sucessfully")
        else:
            print("No such address book")

    def delete_contact(self):

        """
        Method to delete contact from address book
        """
        book_name = input("Enter the address book name ")
        address_book = self.address_books.get(book_name)
        if address_book != None:
            first_name = input("Enter the person name \n")
            contact_to_delete = [contact for contact in address_book if contact.first_name == first_name]
            if len(contact_to_delete) == 0:
                print("Contact not found")
            else:
                address_book.remove(contact_to_delete[0])
                print("Contact removed sucessfully")
        else:
            print("No such address book")