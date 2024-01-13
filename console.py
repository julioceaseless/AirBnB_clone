#!/usr/bin/env python3
"""
console.py - Entry point for the HBNB command interpreter.
"""

import cmd
from models.base_model import BaseModel
from models import storage


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

    def help_quit(self):
        """ quit help """
        print("Quit command to exit the program")

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

    def do_create(self, class_name):
        """
        create a new instance of BaseModel and save to JSON file
        """
        if class_name:
            if class_name != "BaseModel":
                print("** class doesn't exist **")
            else:
                bm1 = BaseModel()
                bm1.save()
                print(bm1.id)
        else:
            print("** class name missing **")

    def do_all(self, class_name):
        """
        Prints all string representation of all instances
        """
        objects = storage.all()
        if class_name:
            if class_name != "BaseModel":
                print("** class doesn't exist **")
            else:
                for key in objects:
                    if key.split('.')[0] == "BaseModel":
                        print([objects[key].__str__()])
        else:
            for key in objects:
                print([objects[key].__str__()])

    def do_update(self, args):
        """ update instance based on class name and id """
        if args:
            cmd_args = args.split(' ', 3)
            # print(cmd_args)
            if len(cmd_args) == 1:
                print("** instance id missing **")
                return
            if len(cmd_args) == 2:
                print("** attribute name missing **")
                return
            if len(cmd_args) == 3:
                print("** value missing **")
                return

            if cmd_args[0] != "BaseModel":
                print("** class doesn't exist **")
                return
            try:
                key = "{}.{}".format(cmd_args[0], cmd_args[1])
                instance = storage._FileStorage__objects[key]
                setattr(instance, cmd_args[2], cmd_args[3].strip('"'))
                storage.save()
            except KeyError:
                print("** no instance found **")
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
