import re, string
from maomihzbot import app

random_keys = {
    'hex': '0123456789abcdef',
    'lower': string.ascii_lowercase,
    'upper': string.ascii_uppercase,
    'alpha': string.ascii_letters,
    'oct': '01234567',
    'bin': '01',
    'dec': string.digits,
    'number': string.digits,
    'symbol': string.punctuation,
    'password': string.ascii_letters + string.digits + string.punctuation,
    'alphanum': string.ascii_letters + string.digits,
}

def parse_range(range_str):
    ''' Range Selector parsing, from selector string to a list

    A Range selector is used to select a range of integers. For example,
    [1,2,3,6,7,9,10,11] can be written as "1-3,6,7,9-11". Comma is used
    to seperate them, and the numbers does not need to be in order. To parse
    the above selector, use:
        parse_range('1-3,6,7,9-11')
    which returns a sorted list of integers.
    '''

    # Seperate the values by comma, and strip white spaces
    elements = [a.strip() for a in range_str.split(',')]
    normal = re.compile('^(\d+)$')
    special = re.compile('^(\d+)-(\d+)$')

    # Use set to prevent repetitive storage
    selection = set()

    for e in elements:
        if not e:
            continue
        # Single Integer match
        m = normal.match(e)
        if m:
            if int(m.group(1)) < 0:
                raise ValueError('Error in %s: Range selection must be positive!' % e)
            selection.add(int(m.group(1)))
            continue

        # Range Integer Match
        m = special.match(e)
        if m:
            start = int(m.group(1))
            end = int(m.group(2))
            if start < 0 or end < 0:
                raise ValueError('Error in %s: Range selection must be positive!' % e)
            if end < start:
                raise ValueError('Error Parsing range %s: End < Start' % e)
            for i in range(start, end + 1):
                selection.add(i)
            continue
        # Non match
        raise ValueError('Error Parsing Range: %s' % e)
    return sorted(selection)

def simple(pass_args=False):
    ''' Simple: a decorator to turn a normal function into a simple bot command
    handlers

    To make a command handler, define a function with one argument 'args' or no
    argument, and return the text to send back to the sender. Decorate the
    function use either simple() for no argument or simple(True) for one argument.
    Then you can use the function to create CommandHandler object directly.
    '''
    def simple_dec(func):
        def reply(bot, update):
            update.message.reply_text(func())
        def reply_args(bot, update, args):
            update.message.reply_text(func(args))
        if pass_args:
            return reply_args
        else:
            return reply
    return simple_dec


def txt(file_name):
    ''' txt is a wrapper for a command that simply returns the content of a text
    file. All text files exist in the txt/ directory. Create CommandHandler object
    by calling CommandHandler('command', txt('file/name.txt')).
    '''
    @simple()
    def reply():
        return app.open_resource('txt/' + file_name, mode='r').read()
    return reply
