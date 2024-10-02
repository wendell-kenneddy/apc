from client import Client
from message import Message
from user import User
import pprint

class App:
  __messages: list[Message] = []
  __users: list[User] = []
  __client = Client()

  def init(self) -> None:
    while True:
      self.__print_app_options()
      option = int(input("Type a valid option: "))

      match option:
        case 1:
          try:
            self.__handle_create_user()
          except Exception as err:
            print(err)
        case 2:
          try:
            self.__handle_client_connect()
            self.__handle_client_connection()
          except Exception as err:
            print(err)
        case 3:
          print("Exiting...")
          exit()
        case _:
          print("Invalid option.")

  def __handle_client_connection(self) -> None:
    while True:
      self.__print_client_options()
      option = int(input("Type a valid option: "))
    
      match option:
        case 1:
          connection_info = self.__client.get_connection_info(self.__users)
          pprint.pp(connection_info)
        case 2:
          messages = self.__client.get_unread_messages(self.__messages)
          pprint.pp(messages)
        case 3:
          sender_phone = input("Type the sender's phone number: ")
          messages = self.__client.get_messages_from(sender_phone, self.__messages)
          pprint.pp(messages)
        case 4:
          recipient_phone = input("Type the message recipient's phone number: ")
          text = input("Type the content of the message: ")
          self.__client.send_message_to(recipient_phone, text, self.__messages)
        case 5:
          self.__client.disconnect()
          print("Client disconnected.")
          break
        case _:
          print("Invalid client option.")

  def __handle_client_connect(self) -> None:
    user_phone = input("Type the user's phone number: ")
    for u in self.__users:
      if u.phone == user_phone:
        self.__client.connect(u.phone)
        return print("Successfully connected to client.")
    raise Exception("No user with given phone number found.")

  def __handle_create_user(self) -> None:
    name = input("Type the user's name: ")
    phone = input("Type the user's phone number: ")
    for u in self.__users:
      if u.phone == phone:
        raise Exception("A user with the given phone number already exists.")
    new_user = User(name, phone)
    self.__users.append(new_user)
    print("User created successfully.")

  def __print_app_options(self) -> None:
    print("1) Create new user;")
    print("2) Connect as user;")
    print("3) Exit.")

  def __print_client_options(self) -> None:
    print("1) Get connection info;")
    print("2) Get unread messages;")
    print("3) Get messages from a sender;")
    print("4) Send message;")
    print("5) Disconnect.")