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
        return True

    def emptyline(self):
        """
        Do nothing on an empty line.
        """
        pass

    def do_create(self, arg):
        """
        Create command to create a new instance of BaseModel.
        """
        if not arg:
            print("** class name missing **")
            return

        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """
        Show command to print the string representation of an instance.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        try:
            class_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return

            instance_id = args[1]
            key = class_name + "." + instance_id
            instances = storage.all()
            if key in instances:
                print(instances[key])
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """
        Destroy command to delete an instance based on class name and id.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        try:
            class_name = args[0]
            if len(args) < 2:
                print("** instance id missing **")
                return

            instance_id = args[1]
            key = class_name + "." + instance_id
            instances = storage.all()
            if key in instances:
                del instances[key]
                storage.save()
            else:
                print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """
        All command to print all string representations of instances.
        """
        args = arg.split()
        instances_list = []

        if not arg:
            for instance in storage.all().values():
                instances_list.append(str(instance))
            print(instances_list)
            return

        try:
            class_name = args[0]
            if class_name not in storage.classes():
                print("** class doesn't exist **")
                return

            for key, value in storage.all().items():
                if key.split('.')[0] == class_name:
                    instances_list.append(str(value))
            print(instances_list)
        except NameError:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
