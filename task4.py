contacts = {}

def parse_input(user_input):
    parts = user_input.strip().lower().split(' ', 1)
    command = parts[0]
    args = parts[1] if len(parts) > 1 else ''
    return command, args

def add_contact(args):
    try:
        name, phone = args.split(',')
        name = name.strip()
        phone = phone.strip()
        if name in contacts:
            return f"Contact '{name}' already exists."
        contacts[name] = phone
        return f"Contact '{name}' added with phone number {phone}."
    except ValueError:
        return "Invalid input. Use: add <name>,<phone>"

def change_contact(args):
    try:
        name, phone = args.split(',')
        name = name.strip()
        phone = phone.strip()
        if name not in contacts:
            return f"Contact '{name}' not found."
        contacts[name] = phone
        return f"Contact '{name}' updated with new phone number {phone}."
    except ValueError:
        return "Invalid input. Use: change <name>,<phone>"

def show_phone(args):
    name = args.strip()
    phone = contacts.get(name)
    if phone:
        return f"Phone number for '{name}' is {phone}."
    else:
        return f"Contact '{name}' not found."

def show_all_contacts():
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def main():
    print("Welcome to the assistant bot! Enter 'help' to see available commands.")
    while True:
        user_input = input("Enter command: ")
        command, args = parse_input(user_input)

        if command in ['exit', 'close', 'quit']:
            print("Goodbye!")
            break
        elif command == 'add':
            print(add_contact(args))
        elif command == 'change':
            print(change_contact(args))
        elif command == 'phone':
            print(show_phone(args))
        elif command == 'show':
            print(show_all_contacts())
        elif command == 'help':
            print("Available commands:")
            print("add <name>,<phone> - Add a new contact")
            print("change <name>,<phone> - Change an existing contact")
            print("phone <name> - Show phone number for a contact")
            print("show - Show all contacts")
            print("exit/close/quit - Exit the assistant bot")
        else:
            print("Invalid command. Type 'help' for a list of commands.")

if __name__ == "__main__":
    main()