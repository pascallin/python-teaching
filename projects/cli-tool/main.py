from pyfiglet import Figlet
from prompt_toolkit import prompt

if __name__ == '__main__':
    f = Figlet(font='slant')
    print(f.renderText('pascal cli tool'))
    answer = prompt('Give me some input: ')
    print('You said: %s' % answer)