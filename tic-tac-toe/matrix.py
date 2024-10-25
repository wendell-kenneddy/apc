class Matrix:
  def __init__(self, rows: int, columns: int, default_item: any) ->  None:
    self.rows = rows
    self.columns = columns
    self.data = [None]*rows
    self.default_item = default_item
    
    for i in range(rows):
      self.data[i] = [default_item]*columns

  def insert(self, row: int, column: int, item: any) -> None:
    self.data[row][column] = item

  def delete_item(self, row: int, column: int) -> None:
    self.insert(row, column, self.default_item)

  def get_item(self, row: int, column: int) -> any:
    return self.data[row][column]

  def __str__(self) -> str:
    output = ""

    for i in range(self.rows):
      for j in range(self.columns):
        output += f"{self.get_item(i, j)} "
      output += "\n"

    return output

  