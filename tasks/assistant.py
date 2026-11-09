def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    try:
        name, phone = args
    except ValueError:
        return "Please provide 2 arguments to the command: [add username phone], e.g. 'add Liza 0746634982'"
    if contacts.get(name):
        old_contact = contacts[name]
        return f"Contact already exists with number '{old_contact}'. If you want to change phone for this contact, use command 'change username new_phone'."
    else:
        contacts[name] = phone
        return "Contact added."

def change_contact(args, contacts):
    try:
        name, phone = args
    except ValueError:
        return "Please provide 2 arguments to the command: [change username phone], e.g. 'change Liza 0746634982'"
    if not contacts.get(name):
        return f"No contact found. If you want to add new contact, use command 'add username phone'."
    else:
        contacts[name] = phone
        return "Contact updated."

def show_phone(args, contacts):
    try:
        assert len(args)==1
    except AssertionError:
        return "Please provide 1 argument to the command: [show], e.g. 'phone Liza'"
    name = args[0]
    if not contacts.get(name):
        return f"No contact found."
    else:
        phone = contacts[name]
        return phone

def show_all(contacts):
    return "\n".join([": ".join((k,v)) for k, v in contacts.items()])

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        try:
            command, *args = parse_input(user_input)
        except ValueError:
            print('Please enter a command. Available commands: add / change / phone / all / close / exit.')
            continue

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
