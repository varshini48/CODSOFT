contacts = {}

def display_contacts():
    if not contacts:
        print("Contact list is empty.")
        return
    print("\n--- Contact List ---")
    for name, info in contacts.items():
        print(f"Name: {name}")
        print(f"  Phone: {info['phone']}")
        print(f"  Email: {info['email']}")
        print(f"  Address: {info['address']}")
        print("---------------------")

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    print("Contact added successfully.")

def search_contact():
    key = input("Enter name or phone number to search: ")
    found = False
    for name, info in contacts.items():
        if key.lower() in name.lower() or key in info['phone']:
            print(f"Found contact:\nName: {name}")
            print(f"  Phone: {info['phone']}")
            print(f"  Email: {info['email']}")
            print(f"  Address: {info['address']}")
            found = True
    if not found:
        print("Contact not found.")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print("Leave blank to keep the current value.")
        phone = input(f"Enter new phone (current: {contacts[name]['phone']}): ") or contacts[name]['phone']
        email = input(f"Enter new email (current: {contacts[name]['email']}): ") or contacts[name]['email']
        address = input(f"Enter new address (current: {contacts[name]['address']}): ") or contacts[name]['address']
        contacts[name] = {'phone': phone, 'email': email, 'address': address}
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

while True:
    print("\n--- Contact Management ---")
    print("1. Add new contact")
    print("2. Search contact")
    print("3. View all contacts")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Exit")
    
    choice = input("Enter choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        display_contacts()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
