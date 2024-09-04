list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

def selection_sort(list):
  for x in range(len(list)):
    min_index = x

    for y in range(x + 1, len(list)):
      if list[y] < list[x]: min_index = y
    
    temp = list[x]
    list[x] = list[min_index]
    list[min_index] = temp
    
selection_sort(list)
print(list)