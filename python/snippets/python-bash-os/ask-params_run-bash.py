import os
import subprocess

"""
Challenge:
- Create a menu prompting to allow the user to select an option.
- Execute bash scripts based on the user's selection.
- Do not stop the execution if a script fails.
- If an error ocurrs print which script failed and
  continue to the next script.
- Allow the user to exit the program.
"""

menu_options = {
    '1': '1. Say Hi',
    '2': '2. Say Bye',
    '0': '0. Exit'
}

file_names = [
    'hi',
    'bye',
]


class ExecuteShellScripts:
    def __init__(self):
        pass

    def create_file(self):
        pass


def main():
    is_user_continue = True
    while is_user_continue:
        print(f'-------{os.linesep}Select an option:')
        for option in menu_options:
            print(menu_options[option])

        user_option = input(f'{os.linesep}Option > ')
        if user_option == '0':
            is_user_continue = False
            print(f'{os.linesep}Bye!')
        elif user_option in menu_options \
            and user_option != '0':
            execute_scripts = ExecuteShellScripts()
        else:
            print(f'{os.linesep}Invalid option')



if __name__ == '__main__':
    main()
