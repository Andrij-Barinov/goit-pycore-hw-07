from commands import add_contact, change_contact, show_phone, show_all, add_birthday, show_birthday, birthdays
from utils import parse_input, input_error
from models import AddressBook

def main():
    # The main function for launching a bot
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            # Ending the work of the bot
            print("Good bye!")
            break
        elif command == "hello":
            # Welcome to the user
            print("How can I help you?")
        elif command == "add":
            # Add a contact
            print(add_contact(args, book))
        elif command == "change":
            # Change an existing contact
            print(change_contact(args, book))
        elif command == "phone":
            # Search for a phone by name
            print(show_phone(args, book))
        elif command == "all":
            # Show all contacts
            print(show_all(book))
        elif command == "add-birthday":
            # Add a birthday to a contact
            print(add_birthday(args, book))
        elif command == "show-birthday":
            # Show a contact's birthday
            print(show_birthday(args, book))
        elif command == "birthdays":
            # Show birthdays that will take place within the next week
            print(birthdays(args, book))
        else:
            # Unknown team
            print("Invalid command.")

if __name__ == "__main__":
    main()