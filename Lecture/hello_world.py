import argparse

def hello_world(target:str, repeat:int, goodbye:bool) -> str:
    ''' Generate greeting text for saying hello

    Given a target name, and the number of repeats, 
    and whether or not to say goodbye, this function prints
    the specified greetings to the console.

    Parameters
    ----------
    target : str
        Name of the target to greet

    repeat : int
        Repeat the greeting this number of times

    goodbye : bool
        Whether or not to say goodbye instead of hello

    Returns
    -------
    greeting : str
        The full text of the greeting that is also printed to console.
    '''
    if goodbye == True:
        greeting = 'Goodbye'
    else:
        greeting = 'Hello'

    greeting_text = ''
    for _ in range(repeat):
        greeting_text += f'{greeting} {target}!' + '\n'

    return greeting_text


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                        description='Say Hello to things')
    parser.add_argument('target', help='Name of person to greet')
    parser.add_argument('--repeat', 
                        '-r', 
                        type=int, 
                        default=1, 
                        help="Number of times to greet")
    parser.add_argument('--goodbye', 
                        '-g', 
                        action='store_true',
                        help='Say goodbye instead of hello')

    args = parser.parse_args()

    hello_world(args.target, args.repeat, args.goodbye)
