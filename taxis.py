def find_nearest_taxi(taxis_x, taxis_y, user_x, user_y):
  nearest = ((taxis_x[0] - user_x) ** 2 + (taxis_y[0] - user_y) ** 2) ** 0.5
  nearest_index = None

  for i in range(1, len(taxis_x)):
    distace = ((taxis_x[i] - user_x) ** 2 + (taxis_y[i] - user_y) ** 2) ** 0.5
    if distace < nearest:
      nearest = distace
      nearest_index = i

  return nearest_index

def main():
  taxis_x = [21, 40, 35, 17, -42, 82, 60, -1, -15, 25, 29, 0]
  taxis_y = [25, 30, -1, 45, -20, 60, 0, 26, -10, 52, 36, -1]
  print(find_nearest_taxi(taxis_x, taxis_y, 10, 8))

main()
