from AddressBookConsoleService import AddressBookConsoleService

ADD_CONTACT = 1
DISPLAY_CONTACT = 2
EXIT = 3


if __name__ == "__main__":
    console_service = AddressBookConsoleService()
    print("Welcome to Address Book Management System")

    while True:
        print(" 1 Add Contact ",
        "\n 2 Display Contact",
        "\n 3 Exit")
        user_choice = int(input())
        if user_choice == ADD_CONTACT:
            console_service.add_contact()
        elif user_choice == DISPLAY_CONTACT:
            console_service.display_contact()
        elif user_choice == EXIT:
            print("Thanks for using us ")
            exit()
        else:
            print("Invalid choice")
