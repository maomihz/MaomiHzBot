from random import choice, sample
from base64 import b64encode
from uuid import uuid4

from .util import parse_range, random_keys, simple
from maomihzbot import app

@simple(True)
def random(args):
    try:
        length = int(args[0])
    except IndexError:
        length = 20
    except ValueError:
        return 'Argument Error: Invalid length!'

    if length < 1 or length > 512:
        return 'Argument Error: Length can only be 1-512! /help'

    try:
        format = args[1].lower()
    except IndexError:
        format = 'hex'

    if format not in random_keys:
        return 'Argument Error: Invalid format! /help'

    return ''.join([choice(random_keys[format]) for a in range(length)])

@simple(True)
def b64(args):
    if len(args) < 1:
        return 'Please specify the string to encode! /help'
    msg = [b64encode(i.encode('utf-8')).decode('utf-8') for i in args]
    return '\n'.join(msg)

@simple(True)
def fortune(args):
    fortunes = list(filter(None, app.open_resource('txt/fortune.txt', mode='r').read().split('\n')))
    if not fortunes:
        return 'No fortunes configured'
    return choice(fortunes)

@simple(True)
def randint(args):
    try:
        R = parse_range(args[0])
    except IndexError:
        R = list(range(1,101)) #Default 1-100
    except ValueError as e:
        return str(e)

    try:
        C = int(args[1])
    except:
        C = 1

    if C > 20:
        return 'You can only select 20 at a time!'

    return '\n'.join([str(choice(R)) for i in range(C)])

@simple(True)
def randsample(args):
    try:
        R = parse_range(args[0])
    except IndexError:
        R = list(range(1,101)) #Default 1-100
    except ValueError as e:
        return str(e)

    try:
        C = int(args[1])
    except:
        C = 1

    if C > 20:
        return 'You can only select 20 at a time!'

    try:
        msg = sample(R, C)
    except ValueError as e:
        return str(e)

    return '\n'.join(map(str, sorted(msg)))

@simple()
def uuid():
    return str(uuid4())
