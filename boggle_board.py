import random
import string


class BoggleBoard:
    dice_faces = ["AAEEGN", "ELRTTY", "AOOTTW", "ABBJOO", "EHRTVW", "CIMOTU", "DISTTY",
                  "EIOSST", "DELRVY", "ACHOPS", "HIMNQU", "EEINSU", "EEGHNW", "AFFKPS", "HLNNRZ", "DEILRX"]

    def __init__(self):
        self.board = [["_", "_", "_", "_"], ["_", "_", "_", "_"],
                      ["_", "_", "_", "_"], ["_", "_", "_", "_"]]
        BoggleBoard.print_board(self)

    def shake(self):
        for index1, inner_array in enumerate(self.board):
            for inner_index in range(4):
                inner_array[inner_index] = random.choice(
                    self.dice_faces[inner_index + 4 * index1])
        BoggleBoard.print_board(self)

    def include_word(self, word_to_look_for):
        current_checked_str = ""

        # check horizontal, forwards and backwards
        for inner_array in self.board:
            current_checked_str = "".join(inner_array)
            if (word_to_look_for == current_checked_str):
                return True
            elif (word_to_look_for == current_checked_str[::-1]):
                return True

        # check vertical, forwards and backwards.
        for y in range(4):
            current_checked_str = ""
            for x in range(4):
                current_checked_str += self.board[x][y]
            if (word_to_look_for == current_checked_str):
                return True
            elif (word_to_look_for == current_checked_str[::-1]):
                return True

        # check diag, forwards and backwards

        # if exist, return that it exists. else, return doesn't exist

    def print_board(self):
        for inner_list in self.board:
            for i in inner_list:
                if (i == "Q"):
                    print("Qu", end=" ")
                else:
                    print(i, end="  ")
            print()


board1 = BoggleBoard()
print()
board1.shake()
print()
guess = input("guess: ")
print()
print(board1.include_word(guess))
