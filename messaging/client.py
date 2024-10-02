from message import Message
from user import User

class Client:
  __client_phone: str = ""

  def connect(self, client_phone: str) -> None:
    self.__client_phone =  client_phone

  def disconnect(self) -> None:
    self.__client_phone = ""

  def get_connection_info(self, users: list[User]) -> dict[User]:
    self.__validate_client_phone()
    for u in users:
      if u.phone == self.__client_phone:
        return u.__dict__

  def send_message_to(self, recipient_phone: str, text: str, database: list[Message]) -> None:
    self.__validate_client_phone()
    message = Message(self.__client_phone, recipient_phone, text)
    database.append(message)
    print("Message successfully sent.")

  def get_messages_from(self, sender_phone: str, database: list[Message]) -> list[Message]:
    self.__validate_client_phone()
    messages: list[Message] = []

    for m in database:
      if m.sender_phone == sender_phone and m.recipient_phone == self.__client_phone:
        if not m.read: m.read = True
        messages.append(m.__dict__)
    
    return messages
  
  def get_unread_messages(self, database: list[Message]) -> list[Message]:
    self.__validate_client_phone()
    messages: list[Message] = []

    for m in database:
      if m.recipient_phone == self.__client_phone and not m.read:
        m.read = True
        messages.append(m.__dict__)
    
    return messages
  
  def __validate_client_phone(self) -> None:
    if not self.__client_phone:
      raise Exception("No user connected to this client.")