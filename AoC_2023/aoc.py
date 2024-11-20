import requests
import os

class AoC:
    
    @staticmethod
    def load_puzzle_input(day_no: int , file_name = 'input', split_lines=True):
    
        url = f'https://adventofcode.com/2023/day/{day_no}/input'
        #session = '53616c7465645f5f3cc435cfc8a07e45a89735ffcd3b3fff1682cd6ca637b4b5d03b236efa446f85ca9818be9539447efc56530a2b00234359de736a80d7f26e'
        session = '53616c7465645f5f68534ee5b3ff7e4df2ae63fdc25315bd3c6221412fa1ef99f5e9baef6e4537520d9ca3b8fb615ab53e87e936ad0090ad1cdd2230528abb3f'

        file_path_and_name = f'.\\day\\{"{:02d}".format(day_no)}\\{file_name}'

        if not os.path.exists(file_path_and_name):
            try:
                os.mkdir(f'.\\day\\{"{:02d}".format(day_no)}')
            except:
                pass

            sess = requests.session()
            sess.cookies.set('session', session)
            ret = sess.get(url)
            with open(file_path_and_name, 'w') as f:
                f.write(ret.text) 

        with open(file_path_and_name, 'r') as f:
        # using splitlines removes the newline characters from the input
            ret = f.read()
        
        if split_lines:
            return ret.splitlines()
        else:
            return ret
        
    @staticmethod
    def flip_row_cols(pattern):

        # utility function that flips a 2 dimensional list. 
        # equivalent of reflecting the tl-br diagonal
        #
        # eg:  [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]   becomes: [ [1, 4, 7], [2, 5, 8], [3, 6, 9]]
        #
        cols = []
        for x in range(len(pattern[0])):
            cols.append([pattern[y][x] for y in range(len(pattern)-1, -1, -1)])
        return cols

    @staticmethod
    def rotate_cw(pattern):

        # utility function that rotates a 2 dimensional list clockwise 
        #
        # eg:       [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
        # becomes:  [[10, 7, 4, 1], [11, 8, 5, 2], [12, 9, 6, 3]]
        #

        rows = []
        for x in range(len(pattern[0])):
            rows.append([pattern[y][x] for y in range(len(pattern)-1, -1, -1)])
        return rows

    @staticmethod
    def rotate_ccw(pattern):

        # utility function that rotates a 2 dimensional list counter-clockwise 
        #
        # eg:       [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
        # becomes:  [[3, 6, 9, 12], [2, 5, 8, 11], [1, 4, 7, 10]]
        #

        rows = []
        for x in range(len(pattern[0])-1, -1, -1):
            rows.append([pattern[y][x] for y in range(len(pattern))])
        return rows
    
    @staticmethod
    def test():
        input = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
        expected = [[10, 7, 4, 1], [11, 8, 5, 2], [12, 9, 6, 3]]
        actual = AoC.rotate_cw(input)
        assert expected == actual
        expected = [[3, 6, 9, 12], [2, 5, 8, 11], [1, 4, 7, 10]]
        actual = AoC.rotate_ccw(input)
        assert expected == actual
        actual = AoC.rotate_ccw(AoC.rotate_ccw(AoC.rotate_ccw(AoC.rotate_ccw(input))))
        assert input == actual
        print('Passed.')

AoC.test()