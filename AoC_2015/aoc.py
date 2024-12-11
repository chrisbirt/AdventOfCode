import requests
import os


class AoC:
    
    @staticmethod
    def load_puzzle_input(year: int, day: int , test_file = False, split_lines=True):

        url = f'https://adventofcode.com/{year}/day/{day}/input'
        session = '53616c7465645f5f203c06c14f7984ba7bf9d15715fc9d41c0336e4dd20a716f109271e31ce9d63192f064d4b6fdb180e0008b68a8c85dfbe13782632c671308'

        file_name = 'input_test' if test_file else 'input'

        file_path_and_name = f'.\\day\\{"{:02d}".format(day)}\\{file_name}'

        if not os.path.exists(file_path_and_name):
            try:
                os.mkdir(f'.\\day\\{"{:02d}".format(day)}')
            except:
                pass

            if test_file:
                # create empty test input file
                with open(file_path_and_name, 'w') as f:
                    f.write('') 
            else:
                # get input file from AoC
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
    def get_all_inputs(year: int):
        _ = [AoC.load_puzzle_input(year, day) for day in range(1, 26)]

AoC.get_all_inputs(2015)