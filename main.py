from models import AddressBook
from utils import parse_input, help_text
from commands import (
    handle_add,
    handle_change,
    handle_phone,
    handle_all,
    handle_delete,
    handle_addphone,
    handle_removephone,
    handle_find,
)


def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    print("Type 'help' to see available commands.")
    while True:
        user_input = input("Enter a command: ").strip()
        if not user_input:
            continue

        command, args = parse_input(user_input)

        if command in ("close", "exit"):
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "help":
            print(help_text())
        elif command == "add":
            print(handle_add(args, book))
        elif command == "change":
            print(handle_change(args, book))
        elif command == "phone":
            print(handle_phone(args, book))
        elif command == "all":
            print(handle_all(args, book))
        elif command == "delete":
            print(handle_delete(args, book))
        elif command == "addphone":
            print(handle_addphone(args, book))
        elif command == "removephone":
            print(handle_removephone(args, book))
        elif command == "find":
            print(handle_find(args, book))
        else:
            print("Invalid command. Type 'help' to see available commands.")


if __name__ == "__main__":
    main()
