def main():
  fixed_amount = float(input("Digite o salário fixo: "))
  commission_value = float(input("Digite o valor da comissão: "))
  total_sales_value = float(input("Digite o total arrecadado pelas vendas: "))
  cars_sold = int(input("Digite o total de carros vendidos: "))
  salary = fixed_amount + cars_sold * commission_value + 0.05 * total_sales_value
  print(f"O salário final é igual a R$ {salary}")

main()