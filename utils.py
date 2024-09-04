def _split(string):
  list = []

  for i in range(len(string)):
    list.append(string[i])

  return list

def _join(list):
  string = ""

  for x in list:
    string += str(x)

  return string
