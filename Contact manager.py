import json
import os

CONTACTS_FILE = "contacts.json"


def load_contacts():
    """Load contacts from the JSON file."""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    return {}


def save_contacts(contacts):
    """Save contacts to the JSON file."""
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)
    print("✅ Contacts saved successfully.")


def add_contact(contacts):
    """Add a new contact."""
    print("\n--- Add New Contact ---")
    name = input("Enter name: ").strip()
    if not name:
        print("❌ Name cannot be empty.")
        return

    if name in contacts:
        print(f"❌ Contact '{name}' already exists. Use Edit to update.")
        return

    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()

    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print(f"✅ Contact '{name}' added successfully!")


def view_contacts(contacts):
    """Display all contacts."""
    print("\n--- Contact List ---")
    if not contacts:
        print("📭 No contacts found.")
        return

    for i, (name, info) in enumerate(contacts.items(), start=1):
        print(f"\n{i}. Name  : {name}")
        print(f"   Phone : {info['phone']}")
        print(f"   Email : {info['email']}")
    print()


def edit_contact(contacts):
    """Edit an existing contact."""
    print("\n--- Edit Contact ---")
    name = input("Enter the name of the contact to edit: ").strip()

    if name not in contacts:
        print(f"❌ Contact '{name}' not found.")
        return

    print(f"Editing contact: {name}")
    print("(Press Enter to keep the current value)")

    current = contacts[name]
    new_phone = input(f"Phone [{current['phone']}]: ").strip()
    new_email = input(f"Email [{current['email']}]: ").strip()

    if new_phone:
        contacts[name]["phone"] = new_phone
    if new_email:
        contacts[name]["email"] = new_email

    save_contacts(contacts)
    print(f"✅ Contact '{name}' updated successfully!")


def delete_contact(contacts):
    """Delete a contact."""
    print("\n--- Delete Contact ---")
    name = input("Enter the name of the contact to delete: ").strip()

    if name not in contacts:
        print(f"❌ Contact '{name}' not found.")
        return

    confirm = input(f"Are you sure you want to delete '{name}'? (yes/no): ").strip().lower()
    if confirm == "yes":
        del contacts[name]
        save_contacts(contacts)
        print(f"✅ Contact '{name}' deleted successfully!")
    else:
        print("❌ Deletion cancelled.")


def search_contact(contacts):
    """Search for a contact by name."""
    print("\n--- Search Contact ---")
    query = input("Enter name to search: ").strip().lower()
    results = {name: info for name, info in contacts.items() if query in name.lower()}

    if results:
        for name, info in results.items():
            print(f"\nName  : {name}")
            print(f"Phone : {info['phone']}")
            print(f"Email : {info['email']}")
    else:
        print("🔍 No matching contacts found.")


def main():
    """Main menu loop."""
    contacts = load_contacts()

    while True:
        print("\n============================")
        print("   Contact Management System")
        print("============================")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Search Contact")
        print("6. Exit")
        print("============================")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            search_contact(contacts)
        elif choice == "6":
            print("👋 Better Luck Next Time!")
            break
        else:
            print("❌ Invalid option. Please choose between 1-6.")


if __name__ == "__main__":
    main()