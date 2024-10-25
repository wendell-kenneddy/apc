from matrix import Matrix
from tic_tac_toe import TicTacToe

def main() -> None:
  matrix = Matrix(3, 3, '---')
  game = TicTacToe(matrix)
  winner = None
  
  while winner == None:
    print(matrix.__str__())
    print(game.symbols[game.current_player] + "'s turn.")
    move_log =  " "

    while move_log != None:
      print(move_log)
      print("Please use zero-based indexes.")
      row = int(input(f"Which row to place an {game.symbols[game.current_player]}: "))
      column = int(input(f"Which column to place an {game.symbols[game.current_player]}: "))
      move_log = game.place_symbol(row, column)
    
    winner = game.check_for_winner()
    print("===========")

  print(matrix.__str__())
  print(winner)

if __name__ == "__main__":
  main()