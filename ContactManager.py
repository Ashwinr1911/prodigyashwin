import os

CONTACTS_FILE = "contacts.txt"

def load_contacts():
    contacts = {}
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, mode='r') as file:
            for line in file:
                name, phone, email = line.strip().split(',')
                contacts[name] = {"phone": phone, "email": email}
    return contacts

def save_contacts(contacts):
    with open(CONTACTS_FILE, mode='w') as file:
        for name, info in contacts.items():
            file.write(f"{name},{info['phone']},{info['email']}\n")

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print("Contact added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        print("Contact List:")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

def edit_contact(contacts):
    name_to_edit = input("Enter the name of the contact you want to edit: ")
    if name_to_edit in contacts:
        print("Current Contact Information:")
        print(f"Name: {name_to_edit}, Phone: {contacts[name_to_edit]['phone']}, Email: {contacts[name_to_edit]['email']}")
        phone = input("Enter new phone number (leave empty to keep current): ")
        email = input("Enter new email address (leave empty to keep current): ")
        if phone:
            contacts[name_to_edit]['phone'] = phone
        if email:
            contacts[name_to_edit]['email'] = email
        save_contacts(contacts)
        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    name_to_delete = input("Enter the name of the contact you want to delete: ")
    if name_to_delete in contacts:
        del contacts[name_to_delete]
        save_contacts(contacts)
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def main():
    contacts = load_contacts()
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
