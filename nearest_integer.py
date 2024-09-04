def main():
  list = [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 13, 17, 18]
  n = int(input("Type the target number: "))
  nearest = list[0]

  for i in list:
    if i == n: return print(f"{n} is in the list.")
    if abs(n - i) < abs(n - nearest):
      nearest = i

  print(f"Nearest number is {nearest}.")

main()