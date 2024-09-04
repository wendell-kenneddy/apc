def main():
  total = int(input("Digite o valor total: "))
  remainder = total

  bills_100 = total // 100
  remainder -= bills_100 * 100

  bills_50 = remainder // 50
  remainder -= bills_50 * 50

  bills_10 = remainder // 10
  remainder -= bills_10 * 10
  
  bills_5 = remainder // 5
  remainder -= bills_5 * 5

  print(f"R$ {total} pode ser decomposto em {bills_100} notas de R$ 100, {bills_50} notas de R$ 50, {bills_10} notas de R$ 10, {bills_5} notas de R$ 5 e {remainder} notas de R$ 1.")

main()