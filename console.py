#!/usr/bin/env python3
"""
console.py - Entry point for the HBNB command interpreter.
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand - Command interpreter class.
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program using EOF (Ctrl+D).
        """
        print("")  # Print a newline before exiting
        return True

    def emptyline(self):
        """
        Do nothing on an empty line.
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
