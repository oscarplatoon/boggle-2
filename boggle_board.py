# You should re-use and modify your old BoggleBoard class to support the new requirements
import random
import string
import csv
import os
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "./data/dice.csv")

class BoggleBoard:
  
  def __init__(self):
    self.board = ['-'] * 16
    self.dice = []

    # import the dice
    with open(path) as csvfile:
      reader = csv.reader(csvfile)
      for row in reader:
        self.dice += row

  def __str__(self):
    output = ""
    elem_count = 0
    for elem in self.board:
        if elem == 'Q':
          output += 'Qu'+ " "
        else:
          output += elem + "  "

        elem_count += 1
        if elem_count == 4:
          output += "\n"
          elem_count = 0

    return output

  def shake(self):
    for elem_index in range(len(self.board)):
      self.board[elem_index] = random.choice(string.ascii_letters).upper()

  def shake2(self):
    dice_used = [False] * len(self.dice)
    space_rolled = [False] * len(self.board)
    while False in space_rolled:
      space = random.randint(0, 15)
      if not space_rolled[space]:
        while False in dice_used:
          die = random.randint(0, 15)
          if not dice_used[die]:
            self.board[space] = random.choice(self.dice[die])
            dice_used[die] = True
            break
        space_rolled[space] = True

# Essentially, we need to get all 4-letter combinations of letters on the board (vertical, horizontal, diagonal - all forwards and backwards) and see if our 4-letter word that we pass in is on that board.
# Need to check
# all rows forwards and backwards
# all columns up and down
# diagonally across the middle of the board both ways
# break if a match is found

  def include_word(self, word):
      #check rows forward and backwards
      for row_start in range(0, 13, 4):
        #convert the row to a string to check for equality to word
        row = ''.join(self.board[row_start : row_start + 4])
        if word == row:
          return "Found!"
        #reverse the word to check the backwards case
        elif word == row[::-1]:
          return "Found!"
      #check columns forwards and backwards
      for col in range (0, 3):
        column = ''.join(self.board[i] for i in [col, col+4, col+8, col+12])
        if word == column:
          return "Found!"
        elif word == column[::-1]:
          return "Found!"

      #check diagonal forwards and backwards
      diagonal = ''.join(self.board[i] for i in [0, 5, 10, 15])
      if word == diagonal:
        return "Found!"
      elif word == diagonal[::-1]:
        return "Found!"
      
      return "Not Found :-("

myBoard = BoggleBoard()
myBoard.board[15] = 'p'
myBoard.board[10] = 'e'
myBoard.board[5] = 'a'
myBoard.board[0] = 'r'
print(myBoard)
print(myBoard.include_word("beer"))