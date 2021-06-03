import random
import time

#fully functional game
#time module is not being used
#still need to fix a user input of "Qu"
#still need to fix user input of double letters (i.e. user guesses "ally")

class BoggleBoard:
      flag = True   #flag to exit main loop (only false with input "q")
      dice =[
      ['A ','A ','E ','E ','G ','N '],['E ','L ','R ','T ','T ','Y '],
      ['A ','O ','O ','T ','T ','W '],['A ','B ','B ','J ','O ','O '],
      ['E ','H ','R ','T ','V ','W '],['C ','I ','M ','O ','T ','U '],
      ['D ','I ','S ','T ','T ','Y '],['E ','I ','O ','S ','S ','T '],
      ['D ','E ','L ','R ','V ','Y '],['A ','C ','H ','O ','P ','S '],
      ['H ','I ','M ','N ','Qu','U '],['E ','E ','I ','N ','S ','U '],
      ['E ','E ','G ','H ','N ','W '],['A ','F ','F ','K ','P ','S '],
      ['H ','L ','N ','N ','R ','Z '],['D ','E ','I ','L ','R ','X ']
      ]
  
      def __init__(self):
            self.board = [['_','_','_','_'],['_','_','_','_'],['_','_','_','_'],['_','_','_','_']]
            self.show_board()
            while self.flag == True:
                  self.ask_response()

      def shake(self):
            self.count = 0
            self.pointer = list(range(0,16))      #order for dice
            random.shuffle(self.pointer)          #randomizes dice order
            for row in range(0,4):                #iterate through each space on the board
                  for space in range(0,4):            
                        self.board[row][space] = self.dice[self.pointer[self.count]][random.randint(0,5)]
                        self.count += 1           #count is used for pointer which specifies which die 
            self.show_board() 

      def show_board(self):
            print(f'\nBoggle Board\n')
            for row in range(0,4):
                  output = ''
                  for space in range(0,4):
                        output += (self.board[row][space]) + ' '
                  print(f'{output}')
            print(f'\n') 

      def ask_response(self):
            self.response = input('Enter "s" to shake\nEnter a four letter word to see if it lies within the Boggle Board ("Qu" counts as one letter)\nEnter "q" to quit: ')
            print(f'\n\n\n\n\n\n\n\n\n\n\n')
            if self.response == 's':
                  self.shake()
            #     elif self.response == 't':
            #       self.shake()
            #       self.start_timer()
            elif self.response != 'q':
                  
                  if(self.include_word(self.response.upper())):
                        print(f'\n\n\n\n\n\n\n\n\n\n\n')
                        print(f'\n{self.response} is found within the boggle board\n')
                        self.show_board()
                  else:
                        print(f'\n\n\n\n\n\n\n\n\n\n\n')
                        print(f'\n{self.response} is not found within the boggle board\n')
                        self.show_board()
            else:
                  self.flag = False

      # def start_timer(self):
      #       self.t = 10
      #       while self.t > 0:
      #             print(f'\r{divmod(self.t,60)}', end ='\r')
      #             self.t -= 1
      #             time.sleep(1)
      #       print(f'\n\n\n\nTIMES UP!!!!\n')

      def include_word(self,word):
            self.check_board =[['_','_','_','_'],['_','_','_','_'],['_','_','_','_'],['_','_','_','_']]
            for row in range(4):
                  for column in range(4):
                        self.check_board[row][column] = self.board[row][column].strip()
            self.letter_index = [[],[],[],[]]

            for i,x in enumerate(word):
                  for row in range(0,4):
                        for column in range(0,4):
                              if self.check_board[row][column] == x:
                                    self.letter_index[i].append([row,column])
                  if(self.letter_index[i] == []):
                        return False
            
            for x in range(0,3):
                  possible = []
                  for first in self.letter_index[x]:
                        for second in self.letter_index[x+1]:
                              if (abs(first[0]-second[0])<=1 and abs(first[1]-second[1])<=1):
                                    possible.append([second[0],second[1]])
                  if possible == []:
                        return False
                  else:
                        self.letter_index[x+1] = possible
      

            return True
      

game = BoggleBoard()
