import requests
import os

    
class AoC:

    @staticmethod
    def load_puzzle_input(day_no: int , test_input = False, split_lines=True):
    
        url = f'https://adventofcode.com/2023/day/{day_no}/input'
        session = '53616c7465645f5f3cc435cfc8a07e45a89735ffcd3b3fff1682cd6ca637b4b5d03b236efa446f85ca9818be9539447efc56530a2b00234359de736a80d7f26e'

        file_name = 'test_input' if test_input else 'input'
        file_path_and_name = f'.\\day\\{"{:02d}".format(day_no)}\\{file_name}'

        if not os.path.exists(file_path_and_name):
            try:
                os.mkdir(f'.\\day\\{day_no}')
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


