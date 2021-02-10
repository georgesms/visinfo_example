from termcolor import colored

def add(a,b):
    print(colored( a+b, 'yellow', attrs=['blink']))
    return a+b
