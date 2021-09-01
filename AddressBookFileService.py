from AddressBookConsoleService import AddressBookConsoleService
import json    
from Contacts import Contact
import csv

class AddressBookFileService:

    JSON_FILE = "resources/address_book.json"
    CSV_FILE = "resources/address_book.csv"

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
                new_contact = contact.__dict__
                try:
                    new_contact.pop("book_name")
                except:
                    pass
                contacts_in_book.append(new_contact)
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
 
    def write_in_csv(self):
        
        """
        Method to write contact details in csv file
        """
        fields = ["first_name","last_name","address","city","state","zip","phone_number","email","book_name"]
        contact_list = self.contact_csv_list_builder()
        with open(self.CSV_FILE,"w") as write_file:
            csv_writer = csv.DictWriter(write_file,fieldnames=fields)
            csv_writer.writeheader()
            csv_writer.writerows(contact_list)
        print("Written sucessfully")
    
    def contact_csv_list_builder(self):

        """
        Method to convert address book in the form for list such that it easily get mapped in csv file
        """
        contact_list = [] 
        contact_dict = {}
        address_books = AddressBookConsoleService.address_books
        for address_book in address_books:
            for contact in address_books.get(address_book):
                contact_dict = contact.__dict__
                contact_dict["book_name"] = address_book
                contact_list.append(contact_dict)
        return contact_list
            

    def read_from_csv(self):

        """
        Method to read contacts from csv file
        """
        contacts_in_csv = []
        with open(self.CSV_FILE,"r") as read_file:
            csv_reader = csv.DictReader(read_file)
            for contact in csv_reader:
                contacts_in_csv.append(contact)
        self.contact_csv_to_object_setter(contacts_in_csv)
        print("Contacts read sucessfullly")
        
    def contact_csv_to_object_setter(self,contacts_in_csv):

        """
        Method to set contact that are read from csv file to contact object
        """
        for contact in contacts_in_csv:    
            address_book_name = contact.get("book_name")
            address_book = AddressBookConsoleService.address_books.get(address_book_name) 
            contact.pop("book_name")
            new_contact = Contact(contact)
            # if book does no already exists then creating a new book
            if address_book == None:
                contact_list = [new_contact]
                AddressBookConsoleService.address_books[address_book_name] = contact_list
            # if book already exsists then adding contact to existing book   
            else:
                address_book.append(new_contact)