def add_one_contact(name, phone, contacts):
  contacts[name] = phone

def view_one_contact(name, contacts):
  phone = contacts[name]
  if not phone: return print("A contact with the provided name does not exist.")
  print(f"Name: {name}; Phone: {phone}")

def view_all_contacts(contacts):

  for contact in contacts.items():
    print(f"Name: {contact[0]}; Phone: {contact[1]}")

def delete_one_contact(name, contacts):
  del contacts[name]

def print_operations():
  print("1) Add contact")
  print("2) Delete contact")
  print("3) View one contact")
  print("4) View all contacts")
  print("5) See available options")
  print("6) Exit")

def main():
  contacts = {}

  print_operations()

  while True:
    option = int(input("Type a valid option: "))

    match option:
      case 1:
        name = input("Type the contact's name: ")
        phone = input("Type the contact's phone number: ")
        add_one_contact(name, phone, contacts)
        print("Contact successfully added/updated.")
      case 2:
        name = input("Type the contact's name: ")
        delete_one_contact(name, contacts)
        print("Contact successfully deleted.")
      case 3:
        name = input("Type the contact's name: ")
        view_one_contact(name, contacts)
      case 4:
        view_all_contacts(contacts)
      case 5:
        print_operations()
      case 6:
        print("Exiting...")
        return
      case _:
        print("Invalid option.")


main()