first_set_string = input("Type the first set of integers: ")
second_set_string = input("Type the second set of integers: ")
first_set_list = []
second_set_list = []
current_integer = ""
distance = 0

for x in range(len(first_set_string)):
  if (first_set_string[x] == " " or x == len(first_set_string) - 1):
    current_integer += first_set_string[x]
    first_set_list.append(int(current_integer))
    current_integer = ""
  else:
    current_integer += first_set_string[x]

for y in range(len(second_set_string)):
  if (second_set_string[y] == " " or y == len(second_set_string) - 1):
    current_integer += second_set_string[y]
    second_set_list.append(int(current_integer))
    current_integer = ""
  else:
    current_integer += second_set_string[y]

if len(first_set_list) != len(second_set_list):
  print("The two sets must be of equal length.")
else:
  for i in range(len(first_set_list)):
    distance += (int(first_set_list[i]) - int(second_set_list[i])) ** 2

  print(f"The euclid distance between the two sets is {distance ** 1/2}")