#!/usr/bin/env python3
"""
console.py - Entry point for the HBNB command interpreter.
"""
import cmd
import re
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.city import City
from models.state import State
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand - Command interpreter class.
    """
    prompt = "(hbnb) "

    def find_match(_str):
        """
        helper function finds matches in custom commands
        sample string: User.show("38f22813-2753-4d42-b37c-57a17f1e4f88")
        """
        full_arg = ""
        class_name = _str.split('.')[0]
        id_string = _str.split('.')[1]
        match = re.search(r'\("([^"]+)"\)', id_string)
        if match:
            obj_id = match.group(1)
        full_arg = class_name + " " + obj_id
        return full_arg

    def default(self, line):
        """ custom commands """

        # custom do_all
        if line.endswith("all()"):
            arg = line.split('.')[0]
            self.do_all(arg)

        # custom count
        if line.endswith("count()"):
            arg = line.split('.')[0]
            self.do_count(arg)

        # custom show eg <class name>.show(<id>)
        if "show(" in line:
            arg = HBNBCommand.find_match(line)
            self.do_show(arg)

        # custom destroy eg <class name>.destroy(<id>)
        if "destroy(" in line:
            arg = HBNBCommand.find_match(line)
            self.do_destroy(arg)

        # custom update command
        if "update(" in line:
            class_name = line.split('.')[0]
            arg_str = line.split('.')[1]
            match = re.search(r'\((.*?)\)', arg_str)
            command_str = ""
            if match:
                command_str = ""
                str_in_brkt = match.group(1)
                result_tuple = tuple(map(str.strip, str_in_brkt.split(',')))
                len_ = len(result_tuple)
                for i in range(len_ - 1):
                    result_tuple[i].strip('"')
                    command_str += result_tuple[i].strip('"') + " "
                command_str += result_tuple[len_ - 1]
            arg = class_name + " " + command_str
            self.do_update(arg)

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

        if len(arg.split()) > 1:
            print("** class doesn't exist **")
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
        if not arg:
            print("** class name missing **")
            return

        class_exists = False
        args = arg.split(' ', 1)
        instances = storage.all()
        class_name = args[0]

        if not HBNBCommand.check_exist(class_name, 0, **instances):
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + "." + instance_id
        if key in instances:
            print(instances[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Destroy command to delete an instance based on class name and id.
        """
        if not arg:
            print("** class name missing **")
            return

        class_exists = False
        args = arg.split(' ', 1)
        instances = storage.all()
        class_name = args[0]

        if not HBNBCommand.check_exist(class_name, 0, **instances):
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + "." + instance_id
        if key in instances:
            del instances[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        All command to print all string representations of instances.
        """
        instances_list = []

        if not arg:
            for instance in storage.all().values():
                instances_list.append(str(instance))
            print(instances_list)
            return

        class_name = arg.split()[0]

        for key, value in storage.all().items():
            if key.split('.')[0] == class_name:
                instances_list.append(str(value))

        if len(instances_list) == 0:
            print("** class doesn't exit **")
        else:
            print(instances_list)

    def check_exist(search_key, pos, **instances):
        item_found = False
        for key in instances.keys():
            if key.split('.')[pos] == search_key:
                item_found = True
                break
        return item_found

    def do_update(self, args):
        """ update instance based on class name and id """
        if args:
            instances = storage.all()
            cmd_args = args.split(' ', 3)
            # print(cmd_args)
            if len(cmd_args) == 1:
                if not HBNBCommand.check_exist(cmd_args[0], 0, **instances):
                    print("** class doesn't exist **")
                    return
                print("** instance id missing **")
                return

            if len(cmd_args) == 2:
                if not HBNBCommand.check_exist(cmd_args[1], 1, **instances):
                    print("** no instance found **")
                    return
                print("** attribute name missing **")
                return

            if len(cmd_args) == 3:
                print("** value missing **")
                return

            instances = storage.all()
            key = "{}.{}".format(cmd_args[0], cmd_args[1])
            if key in instances.keys():
                obj = instances[key]
                setattr(obj, cmd_args[2], cmd_args[3].strip('"'))
                storage.save()
        else:
            print("** class name missing **")

    def do_count(self, obj_type):
        """count number of instances of class"""
        count = 0
        instances = storage.all()
        for key in instances:
            if obj_type == key.split('.')[0]:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
