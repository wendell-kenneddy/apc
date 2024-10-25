from matrix import Matrix

class TicTacToe:
  def __init__(self, matrix: Matrix):
    self.moves_made = 0
    self.matrix = matrix
    self.symbols = { 1: 'X', -1: 'O' }
    self.current_player = 1

  def place_symbol(self, row: int, column: int) -> None | str:
    if self.matrix.get_item(row, column) != self.matrix.default_item:
      return "Invalid position."
    self.matrix.insert(row, column, f"-{self.symbols[self.current_player]}-")
    self.current_player *= -1
    self.moves_made += 1
    return None

  def check_for_winner(self) -> None | str:
    for i in range(self.matrix.rows):
      prev = self.matrix.get_item(i, 0)

      for j in range(self.matrix.columns):
        if self.matrix.get_item(i, j) == self.matrix.default_item or self.matrix.get_item(i, j) != prev: break
        if j == self.matrix.columns - 1: return self.symbols[self.current_player * -1] + " won!"

    for i in range(self.matrix.columns):
      prev = self.matrix.get_item(0, i)

      for j in range(self.matrix.rows):
        if self.matrix.get_item(j, i) == self.matrix.default_item or self.matrix.get_item(j, i) != prev: break
        if j == self.matrix.rows - 1: return self.symbols[self.current_player * -1] + " won!"

    prev = self.matrix.get_item(0, 0)
    for i in range(self.matrix.columns):

      if self.matrix.get_item(i, i) == self.matrix.default_item or self.matrix.get_item(i, i) != prev: break
      if i == self.matrix.columns - 1: return self.symbols[self.current_player * -1] + " won!"
      
    prev = self.matrix.get_item(i, self.matrix.columns - i - 1)
    for i in range(self.matrix.columns):

      if self.matrix.get_item(i, self.matrix.columns - i - 1) == self.matrix.default_item or self.matrix.get_item(i, self.matrix.columns - i - 1) != prev: break
      if i == self.matrix.columns - 1: return self.symbols[self.current_player * -1] + " won!"


    if self.moves_made == 9: return "Draw!"
    return None

    