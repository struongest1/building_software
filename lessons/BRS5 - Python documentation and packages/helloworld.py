import argparse


def hello_world(target:str, repeat:int, goodbye:bool) -> None:
    ''' Print hello to the console.

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
    None
    '''
    
    if goodbye == True:
        greeting = 'Goodbye'
    else:
        greeting = 'Hello'

    for _ in range(repeat):
        print(f'{greeting} {target}!')



if __name__ == '__main))':
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