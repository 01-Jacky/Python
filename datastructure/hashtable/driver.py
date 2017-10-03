""" Driver program to manmually operate hashtable """
import hashtable

class Command:
    def __init__(self, key, description):
        self.key = key
        self.description = description

PRINT = Command('p', 'print representation of hashtable')
SET = Command('s', 'insert item')
GET = Command('g', 'get item')
DELETE = Command('d', 'delete item')
LOAD = Command('l', 'print current load')
QUIT = Command('q', 'quit')
HELP = Command('h', 'show list of commands')

COMMANDS = [
    PRINT,
    SET,
    GET,
    DELETE,
    LOAD,
    QUIT,
    HELP,
]

def print_help():
    format_string = '{} - {:<5}'
    print('List of commands:')
    for command in COMMANDS:
        print(format_string.format(command.key, command.description))
    print()

# Main
action = None
size = int(input('Enter the # of elements to hold in hashtable: '))
hashtable = hashtable.HashTable(size)

print_help()
print('')

while action is not QUIT.key:
    action = input('Enter a command: ')
    try:
        if action is SET.key:
            key = input('key: ')
            value = input('value: ')
            hashtable.set(key, value)
        elif action is GET.key:
            key = input('key: ')
            retrieved = hashtable.get(key)
            if retrieved is None:
                print('Did not find key with value ' + key)
            else:
                print('Retrieved value: ' + retrieved)
        elif action is DELETE.key:
            key = input('key: ')
            deleted = hashtable.delete(key)
            if deleted is None:
                print('Did not find key with value ' + key)
            else:
                print('Deleted value: ' + deleted)
        elif action is LOAD.key:
            print(hashtable.load())
        elif action is PRINT.key:
            hashtable.printBins()
        elif action is HELP.key:
            print_help()
        else:
            print('Command not recongized. Type h for list of command')
        print('')
    except ValueError as e:
        print('Error: {}\n'.format(str(e)))

