def main() -> None:
  filename = input('Type the name of the file containing the words: ')
  src = open(filename, 'r')
  lines = src.readlines()
  target = input('Type the word to search for: ')
  line_length = len(lines[0])

  for i in range(len(lines)):
    row = lines[i]
    horizontal_search_result = row.find(target)
    if horizontal_search_result != -1:
      return print(f"Found word {target} on line {i + 1}, starting from index {horizontal_search_result} to {horizontal_search_result + len(target) - 1}.")
    
  for j in range(line_length):
    column = ""

    for k in range(len(lines)):
      if len(lines[k]) != line_length: return print(f"Line {k + 1} malformed.")
      column += lines[k][j]

    vertical_search_result = column.find(target)
    if vertical_search_result != -1:
      return print(f"Found word {target} on column {j + 1}, starting from index {vertical_search_result} to {vertical_search_result + len(target) - 1}.")

  print("Word not found.")

if __name__ == "__main__":
  main()