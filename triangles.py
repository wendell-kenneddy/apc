def convert_str_to_float(string):
  return float(string)

def main():
  sides = list(map(convert_str_to_float, input("Digite os valores dos lados: ").strip().split(" ")))
  [a, b, c] = sides

  if (a > b + c or b > a + c or c > a + b):
    return print("Não é um triângulo. Um dos lados é maior que a soma dos outros dois.")
  if (a == b and b == c):
    return print("O triângulo é equilátero.")
  if ((a == b and b != c) or (a == c and b == c) or (b == c and a != b)):
    return print("O triângulo é isóceles.")
  print("O triângulo é escaleno.")

main()
