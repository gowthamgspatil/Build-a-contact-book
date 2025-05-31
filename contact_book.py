import json
import os

CONTACTS_FILE = "contacts.json"


def load_contacts():
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, "r") as f:
        return json.load(f)


def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("Contact added successfully.\n")


def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.\n")
    else:
        print("\nAll Contacts:")
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
        print()


def search_contact():
    keyword = input("Enter name or phone to search: ")
    contacts = load_contacts()
    found = False
    for contact in contacts:
        if keyword.lower() in contact['name'].lower() or keyword in contact['phone']:
            print(f"Found: Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            found = True
    if not found:
        print("Contact not found.\n")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    contacts = load_contacts()
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print("Leave field blank to keep current value.")
            new_phone = input(f"New phone (current: {contact['phone']}): ") or contact['phone']
            new_email = input(f"New email (current: {contact['email']}): ") or contact['email']
            contact['phone'] = new_phone
            contact['email'] = new_email
            save_contacts(contacts)
            print("Contact updated successfully.\n")
            return
    print("Contact not found.\n")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    contacts = load_contacts()
    new_contacts = [c for c in contacts if c['name'].lower() != name.lower()]
    if len(contacts) == len(new_contacts):
        print("Contact not found.\n")
    else:
        save_contacts(new_contacts)
        print("Contact deleted successfully.\n")

# Main menu
def main():
    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid option. Please choose between 1-6.\n")

if __name__ == "__main__":
    main()
