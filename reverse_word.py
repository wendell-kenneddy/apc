from utils import _join

def main():
  word = input("Type any word: ")
  temp = []

  for i in range(len(word)):
    temp.append(word[len(word) - 1 - i])

  print(_join(temp))

main()