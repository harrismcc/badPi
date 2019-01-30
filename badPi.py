import sys
import pi
import os

def parseInput():
    ''' This allows the entire program to run in a
        comfortable way from the command line. It
        is a bit dinky. Transition to Click coming

    '''


    def help():
        ''' Prints out the help menu to the user
            A sloppy way of doing this, but functional

        '''
        print()
        print("Welcome to the worst way to calculate pi!")
        print("Add the number of digits you would like as an argument")
        os.system('color 8')
        print("e.g.    >> python badPi.py 5")
        print("or      >> python badPi.py 5 --m 10000")
        os.system('color 7')
        print()
        print('Arguments')
        print("--m     |     allows you to manually specify number of frames")
        print("--h     |     brings up this menu")
        print()

    try:
        digits = int(sys.argv[1])
        environment = pi.platform(digits)
    except: 
        help()
        #some sort of default value to run
        #mostly as an example to user
        sys.argv = ["badPi.py", 5]

        print("Running default for 5 digits (As an example)")
        digits = int(sys.argv[1])
        environment = pi.platform(digits)


    if 'help' in sys.argv or len(sys.argv) <= 1 or '--h' in sys.argv:
        help()
    if '--g' in sys.argv:
        if sys.argv[sys.argv.index("--g") + 1].lower() == "false":
            environment.graphicsEnabled = False

    if '--m' in sys.argv:

        #Try-except in case the user puts the --m flag
        # but does not specify a manual value
        try:
            environment.simulate(sys.argv[sys.argv.index("--m") + 1])
        except(IndexError):
            help()

    else:
        #Normal function, no flags
        environment.autoSimulate()

parseInput()