from AddressBookConsoleService import AddressBookConsoleService

if __name__ == "__main__":
    console_service = AddressBookConsoleService()
    print("Welcome to Address Book Management System")
    contact = console_service.createContact()
    console_service.displayContact(contact)
