"""
This file is a textual UI layer on top of the phone app.
It will allow a user to view, add, and delete contacts,
as well as make calls and send texts.
"""

from phone import Phone

def read_contacts(phone):
    with open('contacts.txt', 'r') as contacts_file:
        for line in contacts_file:
            clean = line.replace(":", '').strip('\n')
            info_list = clean.split(" ")
            phone.add_contact(info_list[0], info_list[1], info_list[2])

def display_menu():
    print '''
        0 - Main Menu
        1 - Show all contacts
        2 - Add a new contact
        3 - Delete a contact
        4 - Make a phone call
        5 - Send a text
        6 - Exit the program
    '''

def display_contacts(phone):

    contacts = phone.contacts.values()
    if contacts:
        for contact in contacts:
            print contact.full_name(), contact.mobile_phone
    else:
        print "No contacts found"

def save_contacts(phone):
    with open('contacts.txt', 'w') as contacts_file:
        contacts = phone.contacts.values()
        for contact in contacts:
            contact_entry = contact.full_name() + ': ' + str(contact.mobile_phone) + '\n'
            contacts_file.write(contact_entry)


def main():

    phone_name = raw_input("Enter the name of your phone: ")
    number = int(raw_input("Enter your number: "))
    phone = Phone(number, phone_name)
    read_contacts(phone)
    print "Congratulations! You've set up your phone!"
    while True:
        display_menu()
        choice = raw_input("Please select an action: ")
        if choice == "0":
            display_menu()
        elif choice == "1":
            display_contacts(phone)
        elif choice == "2":
            first_name = raw_input("Enter the contact's first name: ")
            last_name = raw_input("Enter the contact's last name: ")
            number = int(raw_input("Enter the contact's number: "))
            phone.add_contact(first_name, last_name, number)
            save_contacts(phone)
        elif choice == "3":
            first_name = raw_input("Enter the contact's first name: ")
            last_name = raw_input("Enter the contact's last name: ")
            phone.del_contact(first_name, last_name)
            save_contacts(phone)
        elif choice == "4":
            first_name = raw_input("Enter the contact's first name: ")
            last_name = raw_input("Enter the contact's last name: ")
            phone.call(first_name, last_name)
        elif choice == "5":
            first_name = raw_input("Enter the contact's first name: ")
            last_name = raw_input("Enter the contact's last name: ")
            message = raw_input("Enter the text message: ")
            phone.text(first_name, last_name, message)
        elif choice == "6":
            break
        else:
            print "Invalid selection. Please choose again."



if __name__ == '__main__':
    main()
