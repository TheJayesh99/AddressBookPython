from AddressBookConsoleService import AddressBookConsoleService
import json    
from Contacts import Contact

class AddressBookFileService:

    JSON_FILE = "resources/address_book.json"

    def write_in_json(self):

        """
        Method to write all conatcts  in json file
        """
        address_book = self.address_book_dict_builder()
        with open(self.JSON_FILE,"w") as output_file:
           json_object = json.dumps(address_book,indent=4)
           output_file.write(json_object)
        print("written sucessfully")
    
    
    def address_book_dict_builder(self):

        """
        Method that returns the address book dictionary
        """
        new_address_book_dict = {}
        for address_book in AddressBookConsoleService.address_books:
            contacts_in_book = []
            for contact in AddressBookConsoleService.address_books.get(address_book):
                contacts_in_book.append(contact.__dict__)
            new_address_book_dict[address_book] = contacts_in_book
        return new_address_book_dict

    def read_from_json(self):

        """
        Method to read data from a csv file
        """
        address_books = {}
        with open(self.JSON_FILE,"rb") as read_file:
            address_books_object  = json.loads(read_file.read())
            for address_book_name in address_books_object:
                contact_list = address_books_object[address_book_name]
                new_contact_list = []
                for contact in contact_list:
                    new_contact = Contact(contact)
                    new_contact_list.append(new_contact)
                address_books[address_book_name] = new_contact_list
        AddressBookConsoleService.address_books = address_books
        print("Read contacts sucessfully")
 