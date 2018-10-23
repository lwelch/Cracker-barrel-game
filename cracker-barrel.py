import random

class PlayCrackerBarrelGame(object):
    def __init__(self, rows):
        self.triangle = []
        self.rows = rows
        self.valid_moves = []
        self.number_of_pegs = 0


        #First we set up the default game. Later on, it can be customized to increase the size and/or the starting openings
        self.create_triangle()
        self.random_starting_position()
        for row in self.triangle:
            print(row)
        
        self.find_valid_moves()
        while len(self.valid_moves) is not 0:
            move_num = random.randint(0,len(self.valid_moves)-1)
            self.make_move(self.valid_moves[move_num])
            self.find_valid_moves()

            
            
        if self.number_of_pegs == 1:
                print("Game WON!")
        else:
            print("Game Lost! :(")
            print("Final Board: \n")
            for row in self.triangle:
                print(row)


    def create_triangle(self):
        for row in range(self.rows):
            self.triangle.append([])
            for _ in range(row+1):
                self.triangle[row].append('X')
    
    def random_starting_position(self):
        y_loc = random.randint(0,self.rows-1)
        x_loc = random.randint(0,y_loc)
        self.triangle[y_loc][x_loc] = 'O'


    def find_valid_moves(self):
        self.valid_moves = []
        self.number_of_pegs = 0
        for row_ind, row in enumerate(self.triangle):
            for space_ind, space in enumerate(row):
                if space == 'O':
                     possible_move_locations = self.find_possible_locations(row_ind, space_ind)
                     self.check_if_move_valid(possible_move_locations, row_ind, space_ind)
                else:
                    self.number_of_pegs += 1


    def find_possible_locations(self, row, space):
        possible_move_from_locations = []
        for row_diff in range(-2,4,2):
            for space_diff in range(-2,4,2):
                row_check = row + row_diff
                space_check = space + space_diff

                #Check if valid move and valid space otherwise move to next possible space
                if row_diff * -1 == space_diff or row_check > self.rows-1 or space_check > row_check or space_check > self.rows-1:
                    continue
                if row_check >=0 and space_check >=0:
                    possible_move_from_locations.append({'move from': [row_check, space_check],
                                                         'move over': [row + (row_diff / 2),
                                                                     space + (space_diff / 2)]})

        return possible_move_from_locations

    def check_if_move_valid(self, possible_moves, row, space):
        for move in possible_moves:
            if self.triangle[move['move from'][0]][move['move from'][1]] == 'X' and \
                self.triangle[move['move over'][0]][move['move over'][1]] == 'X':
                move['move to'] =  [row, space]
                self.valid_moves.append(move)

    def make_move(self, move_dict):
        self.triangle[move_dict['move to'][0]][move_dict['move to'][1]] = 'X'
        self.triangle[move_dict['move from'][0]][move_dict['move from'][1]] = 'O'
        self.triangle[move_dict['move over'][0]][move_dict['move over'][1]] = 'O'


PlayCrackerBarrelGame(5)