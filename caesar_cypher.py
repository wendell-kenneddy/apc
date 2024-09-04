alphabet = "abcdefghijklmnopqrstuvwxyz"

def find_new_index(index, offset):
  new_index = index + offset

  if new_index >= len(alphabet):
    diff = new_index - (len(alphabet) - 1)
    return find_new_index(0, diff - 1)

  return new_index

def find_new_letter(char, offset):
  if char == " ": return char
  letter_index = alphabet.index(char)
  new_index = find_new_index(letter_index, offset)
  return alphabet[new_index]

def encrypt(string, offset):
  final = ""

  for x in string:
    final += find_new_letter(x, offset)

  return final

def main():
  base = input("Type a sentence of alphabetic characters: ")
  offset = int(input("Type the offset (integer): "))
  encrypted = encrypt(base, offset)
  print(encrypted)

main()

