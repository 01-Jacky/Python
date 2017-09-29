""" Driver program to manmually operate hashtable """
import hashtable

class Command:
    def __init__(self, key, description):
        self.key = key
        self.description = description

SET = Command('s', 'insert item')
GET = Command('g', 'get item')
DELETE = Command('d', 'delete item')
LOAD = Command('l', 'print current load')
PRINT = Command('p', 'print representation of hashtable')
QUIT = Command('q', 'quit')
HELP = Command('h', 'show list of commands')

COMMANDS = [
    SET,
    GET,
    DELETE,
    LOAD,
    PRINT,
    QUIT,
    HELP,
]

def print_help():
    format_string = '{} - {:<5}'
    print('List of commands:')
    for command in COMMANDS:
        print(format_string.format(command.key, command.description))
    print()


print_help()
action = None
size = int(input('Enter # of bins for hashtable: '))
hashtable = hashtable.HashTable(size)

while action is not QUIT.key:
    action = input('Enter a command: ')
    try:
        if action is SET.key:
            key = input('key: ')
            value = input('value: ')

            hashtable.set(key, value)

        if action is GET.key:
            key = input('key: ')
            retrieved = hashtable.get(key)
            if retrieved is None:
                print('Did not find key with value ' + key)
            else:
                print('Retrieved value: ' + retrieved)
        if action is DELETE.key:
            key = input('key: ')
            print('Deleted value: ' + hashtable.delete(key))
        if action is LOAD.key:
            print(hashtable.load())
        if action is PRINT.key:
            hashtable.printBins()
        if action is HELP.key:
            print_help()
        print('')

    except ValueError as e:
        print('Error: {}\n'.format(str(e)))





