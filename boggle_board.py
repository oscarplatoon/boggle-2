# Ankur's Instructor solution (Boggle-2)

import random

class BoggleDice:
    DICE_FACES = 6

    def __init__(self, values):
        # ensure that have the right number of face values passed in
        assert(len(values) == self.DICE_FACES)
        self.values = values

    def roll(self) -> str:
        # return a random character from our values
        return self.values[random.randint(0, self.DICE_FACES - 1)]


class BoggleBoard:
    BOARD_LENGTH = 4 # length of side

    def __init__(self, dice_list):
        size = self.BOARD_LENGTH ** 2

        # seed empty board with underscores
        self.board = "_" * size
        self.dice_list = dice_list
        
        # ensure that we have enough dice for this board
        assert(len(self.dice_list) == size)
        self.shake()
  
    def shake(self):
        # randomize the dice ordering and roll all dice
        random.shuffle(self.dice_list)
        self.board = ""
        for i in range(self.BOARD_LENGTH ** 2):
            c = self.dice_list[i].roll()
            self.board += c
            
        # print updated board
        self.print_board()

    def print_board(self):
        board_str = ""
        for i in range(len(self.board)):
            c = self.board[i]
            space = "  "

            # handle special case: Q -> Qu
            if (c == "Q"):
                c = "Qu"
                space = " "
            
            # add formatted cell to display string
            board_str += c + space

            # add new line if we're on the last cell for the row
            if ((i+1) % self.BOARD_LENGTH == 0):
                board_str += "\n"
            
        divider_str = "-" * (self.BOARD_LENGTH * 3)
        print(board_str + "\n" + divider_str + "\n")


    def find_word(self, word, found_index_list = None):
        # if word is empty, consider it found
        if word == "":
            return True
        # if the caller didn't pass in a list for tracking indices, create one
        if found_index_list is None:
            found_index_list = []

        search_index_list = list(range(len(self.board)))
        return self.__find_word_helper(word, found_index_list, search_index_list)

    def __find_word_helper(self, word, found_index_list, search_index_list):
        for i in search_index_list:
            # get char from index
            c = self.board[i]
            # handle special case: "Q" -> "Qu"
            if c == "Q":
                c = "Qu"
            
            # continue search if current index char matches the first char of the search word
            # NOTE: we have to check the char length due to the "Qu" case
            if len(c) <= len(word) and c == word[0:len(c)]:
                # add matching index to our list
                found_index_list.append(i)

                # remove the char that we found from our word to search
                word_remaining = word[len(c):]

                # if we have no more chars remaining, we've found our entire word! -> return True
                if (word_remaining == ""):
                    return True

                # determine search space for the next match
                neighbor_index_list = self.get_neighbor_indices(found_index_list[-1], found_index_list)

                # repeat search for remaining letters
                word_found = self.__find_word_helper(
                    word_remaining, 
                    found_index_list, 
                    neighbor_index_list)
                
                if (word_found):
                    return True # reduce call stack

                # if we didn't find our word with this index, remove the last index that we added
                found_index_list.pop()


    def get_neighbor_indices(self, start_index, exclude_index_list):
        neighbor_index_list = []

        valid_N = (start_index - self.BOARD_LENGTH) >= 0
        valid_E = (start_index % self.BOARD_LENGTH) + 1 < self.BOARD_LENGTH
        valid_S = (start_index + self.BOARD_LENGTH) < self.BOARD_LENGTH ** 2
        valid_W = (start_index % self.BOARD_LENGTH) - 1 >= 0

        # store valid neighboring cells (8-directions)
        if (valid_N):
            neighbor_index_list.append(start_index - self.BOARD_LENGTH)
        if (valid_N and valid_E):
            neighbor_index_list.append(start_index - self.BOARD_LENGTH + 1)
        if (valid_E):
            neighbor_index_list.append(start_index + 1)
        if (valid_S and valid_E):
            neighbor_index_list.append(start_index + self.BOARD_LENGTH + 1)
        if (valid_S):
            neighbor_index_list.append(start_index + self.BOARD_LENGTH)
        if (valid_S and valid_W):
            neighbor_index_list.append(start_index + self.BOARD_LENGTH - 1)
        if (valid_W):
            neighbor_index_list.append(start_index - 1)
        if (valid_N and valid_W):
            neighbor_index_list.append(start_index - self.BOARD_LENGTH - 1)

        return filter(lambda index: index not in exclude_index_list, 
            neighbor_index_list)


## main execution point
dice_faces = [
    "AAEEGN", "ELRTTY", "AOOTTW", "ABBJOO", 
    "EHRTVW", "CIMOTU", "DISTTY", "EIOSST", 
    "DELRVY", "ACHOPS", "HIMNQU","EEINSU", 
    "EEGHNW", "AFFKPS", "HLNNRZ", "DEILRX"
]

# intialize dice and board
dice_list = [BoggleDice(dice_str) for dice_str in dice_faces]
bb = BoggleBoard(dice_list)

# grab user input for target word
word_to_find = input("What word do you want to find?: ").upper()

word_found = False
word_indices = []
attempt = 0
# keep shaking and searching until we find out word or hit our max attempts
while (not word_found and attempt < 1000):
    bb.shake()
    word_indices = []
    word_found = bb.find_word(word_to_find, word_indices)
    attempt += 1

print(attempt, ":", word_indices)






