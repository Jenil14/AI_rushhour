from collections import namedtuple, deque
from copy import deepcopy
from vehicle import *


Position = namedtuple('Position', 'y x') 



#Represents the board for the problem
class Board():
    
    def __init__(self, input):
        
        self.cars = dict()
        self.finish = None
        self.width = 0
        self.height = 0
        self.moves = []
        self.parsing(input)

        assert self.finish is not None, "There's no finish on the board."
        assert 'X' in self.cars, "There is no final car on the board."

    def parsing(self, input):
  
        lines = list(map(lambda l: l.strip(), input.strip().split('\n'))) #converts every element of the list to an integer value. 
        self.height = len(lines)
        prev = '-'
        for i, line in enumerate(lines):
            width = len(line.replace('>', ''))
            if self.width == 0:
                self.width = width
            else:
                assert  self.width == width, "Check equality"
            for j, char in enumerate(line):
                if char == '-':
                    pass
                elif char == '>':
                    self.finish = (i, j)
                elif char not in self.cars:
                    self.cars[char] = Car(char, Position(i, j), 1)
                else:
                    self.cars[char].size += 1
                    self.cars[char].is_horizontal = (char == prev)
                prev = char

    def get_position_contents(self, pos):
  
        for k, piece in self.cars.items():
            if (piece.pos.x <= pos.x <= piece.end.x 
              and piece.pos.y <= pos.y <= piece.end.y):
                return piece
        return None

    def get_child_states(self):
       
        states = []
        max_moves = max(self.width, self.height)
        for k, piece in self.cars.items():
            for direction in (-1,1):
                offset = direction
                is_valid = True
                while is_valid:
                    pos = piece.get_new_pos(offset)
                    is_valid = self.is_valid_position(pos)
                    if is_valid:
                        states.append(self.make_state(Movement(k, offset)))
                    offset += direction
        return states

    def is_valid_position(self, pos):
        
        if 0 <= pos.y < self.height and 0 <= pos.x < self.width:
            if self.get_position_contents(pos) is None:
                return True
        return False

    def make_state(self, move):
        
        state = deepcopy(self)
        state.move_car(move)
        return state

    def move_car(self, move):
     
        self.moves.append(move)
        car = self.cars[move.obj]
        car.move(move.direction)

    def __str__(self):
        state = []
        for key in sorted(self.cars.keys()):
            state.append("{}({},{},{})".format(key, self.cars[key].pos.y, 
                self.cars[key].pos.x, 0 if self.cars[key].is_horizontal else 1))
        return ":".join(state)
      

 
class Movement():

    #Represents the distance the car moves
   
    def __init__(self, obj, direction):
        
        self.obj = obj
        self.direction = direction

    def __str__(self):
        return "{} {:+}".format(self.obj, self.direction)
