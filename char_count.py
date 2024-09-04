def reduce(iterable, callback, initialValue):
  accumulator = initialValue

  for x in iterable:
    accumulator = callback(accumulator, x)

  return accumulator

def count_letters(acc, curr):
  if not acc.get(curr):
    acc[curr] = 1
  else:
    acc[curr] += 1

  return acc

def main():
  word = input("Type any word: ")
  record = reduce(word, count_letters, {})
  print(record)

main()

