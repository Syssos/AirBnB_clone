#!/usr/bin/env python3
""" This is a command interpreter for the AirBnB clone
"""
import cmd
import sys
import shlex
import models
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User


class HBNBCommand(cmd.Cmd):

    instances_of = []

    def emptyline(self):
        """ Prints empty line
        """
        pass

    def do_EOF(self, args):
        """ Ctrl + D will exit program
        """
        return True

    def do_quit(self, args):
        """ Quit command to exit program
        """
        raise SystemExit

    def do_create(self, args):
        """
        """
        if len(args) is 0:
            print('** class name missing **')
        elif args == "BaseModel":
            new = BaseModel()
            new.save()
            print(new.id)
        elif args == "User":
            new_1 = User()
            new_1.save()
            print(new_1.id)
        else:
            print('** class doesn\'t exist **')

    def do_show(self, args):
        """
        """
        args = shlex.split(args)
        if len(args) is 0:
            print('** class name missing **')
        if len(args) is 1:
            print('** instance id missing **')
        if args[0] != "BaseModel" and args[0] != "User":
            print('** class doesn\'t exist **')
        else:
            key = "{}.{}".format(args[0], args[1])
            new_dict = models.storage.all()
            if key in new_dict:
                print(new_dict[key])
            else:
                print('** no instance found **')

    def do_destroy(self, args):
        """
        """
        args = shlex.split(args)
        if len(args) is 0:
            print('** class name missing **')
        if len(args) is 1:
            print('** instance id missing **')
        if args[0] != "BaseModel" and args[0] != "User":
            print('** class doesn\'t exist **')
        else:
            key = "{}.{}".format(args[0], args[1])
            new_dict = models.storage.all()
            if key in new_dict:
                del new_dict[key]
                models.storage.save()
            else:
                print('** no instance found **')

    def do_all(self, args):
        """
        """
        args = shlex.split(args)
        if len(args) > 0 and args[0] != 'BaseModel' and args[0] != 'User':
            print('** class doesn\'t exist **')
        else:
            temp_dict = models.storage.all()
            for x in temp_dict:
                print([temp_dict[x]])

    def do_update(self, args):
        """
        """
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 4:
            class_id = "{}.{}".format(args[0], args[1])
            setattr(models.storage.all()[class_id], args[2], args[3])
            models.storage.all()[class_id].save()
        else:
            print("** value missing **")


if __name__ == '__main__':
    prompt = HBNBCommand()
    prompt.prompt = '(hbnb) '
    prompt.cmdloop()
