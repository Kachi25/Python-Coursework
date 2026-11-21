
# Python Essentials 1
# Project: Contact Book Application

# Create a dictionary to store contacts and phone numbers
contacts = {}


# 1. Function to add a contact
def add_contact(contacts):

    name = input("Enter contact name: ").strip()

    # Check if the name already exists
    for existing_name in contacts:
        if existing_name.lower() == name.lower():
            print(f"Contact {name} already exists.")
            return

    if not name:
        print("Name cannot be empty.")
        return

    phone_number = input("Enter phone number: ").strip()

    # Validate phone number
    if not phone_number.isdigit() or len(phone_number) < 7 or len(phone_number) > 15:
        print("Invalid phone number. Enter 7-15 digits.")
        return

    contacts[name] = phone_number

    print(f"Contact {name} added successfully!")


# 2. Function to view all contacts
def view_contacts(contacts):

    if not contacts:
        print("Your contact list is empty.")

    else:
        print("\nYour Contacts:")

        for name, phone_number in contacts.items():
            print(f"Name: {name} | Phone: {phone_number}")


# 3. Function to search for a contact
def search_contact(contacts):

    name = input("Enter the name you want to search for: ").strip()

    found = False

    for contact_name, phone_number in contacts.items():

        if name.lower() in contact_name.lower():
            print(f"Name: {contact_name} | Phone: {phone_number}")
            found = True

    if not found:
        print(f"No contact found matching {name}.")


# 4. Function to delete a contact
def delete_contact(contacts):

    name = input("Enter the name of the contact to delete: ").strip()

    for contact_name in contacts:

        if contact_name.lower() == name.lower():

            del contacts[contact_name]

            print(f"Contact {contact_name} deleted successfully!")
            return

    print(f"Contact {name} was not found.")


# 5. Main menu function
def main():

    while True:

        print("\n========== CONTACT BOOK MENU ==========")
        print("1. Add New Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        print("=======================================")

        try:
            choice = int(input("Enter your choice (1-5): "))

        except ValueError:
            print("Invalid input. Please enter a number from 1 to 5.")
            continue

        if choice == 1:
            add_contact(contacts)

        elif choice == 2:
            view_contacts(contacts)

        elif choice == 3:
            search_contact(contacts)

        elif choice == 4:
            delete_contact(contacts)

        elif choice == 5:
            print("Thank you for using the Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 5.")


# Start the application
main()
