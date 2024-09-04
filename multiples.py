def main():
  x = int(input("Digite o primeiro número: "))
  y = int(input("Digite o segundo número: "))
  if (x % y == 0 or y % x == 0): return print("São múltiplos.")
  print("Não são múltiplos.")

main()