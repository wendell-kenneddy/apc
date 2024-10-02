from datetime import datetime

class Message:
  def __init__(self, sender_phone: str, recipient_phone: str, text: str) -> None:
    self.sender_phone = sender_phone
    self.recipient_phone = recipient_phone
    self.text = text
    self.read = False
    self.created_at = datetime.now()
