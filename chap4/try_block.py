#!/usr/bin/env python3

class CustomError(Exception):
    pass

try:
    try:
        s = input("Please type 'e': ")
        """
        The user could also break out of the loop, and indeed out of the 
        entire program, by typing Ctrl+C—this would cause a KeyboardInterrupt 
        exception to be raised, and since this is not handled by any of the 
        program’s exception handlers, would cause the program to terminate 
        and print a traceback. Should we leave such a “loophole”? If we don’t, 
        and there is a bug in our program, we could leave the user stuck in an 
        infinite loop with no way out except to kill the process. Unless there 
        is a very strong reason to prevent Ctrl+C from terminating a program, 
        it should not be caught by any exception handler.
        """
    except EOFError as err:
        print("EOF Error! You can't shut me down!")
        exit()
    """
    except (EOFError, KeyboardInterrupt) as err:
        if isinstance(err, EOFError):
            error = "EOF Error! You can't shut me down!"
        elif isinstance(err, KeyboardInterrupt):
            error = "Keyboard Interrupt! You can't interrupt me!"
        print(error)
        exit()
    """

    if s == 'e':
        print("Thank you!")
    else:
        raise CustomError("It's not 'e'!")
except CustomError:
    print("You are not following, dude! But I can finish the program!")

