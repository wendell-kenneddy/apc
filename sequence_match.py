from utils import _join, _split

def main():
  list = input("Type a list of integers separated by blank spaces: ").split(" ")
  sequence = input("Type two integers separated by blank spaces (order will be preserved): ").split(" ")

  if len(list) < 2: return print("Not enough characters.")

  for i in range(len(list) - 1):
    if (list[i] == sequence[0] and list[i + 1] == sequence[1]): return print("The sequence appears in the list.")
  
  print("The sequence does not appear in the list.")

main()