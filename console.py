#!/usr/bin/env python3
""" This is a command interpreter for the AirBnB clone
"""
import cmd, sys, shlex, models, json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


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
            print ('** class name missing **')
        elif args != "BaseModel":
            print('** class doesn\'t exist **')
        else:
            new = BaseModel()
            new.save()
            print(new.id)

    def do_show(self, args):
        """
        """
        args = shlex.split(args)
        if len(args) is 0:
            print('** class name missing **')
        if len(args) is 1:
            print('** instance id missing **')
        if args[0] != "BaseModel":
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
        if args[0] != "BaseModel":
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
        if args != 'BaseModel':
            print('** class doesn\'t exist **')
        temp_dict = models.storage.all()
        for x in temp_dict:
            print([temp_dict[x]])
    
    def do_update(self, args):
        """
        """
        args = shlex.split(args)
        

#FileStorage.__file_path
if __name__ == '__main__':
    prompt = HBNBCommand()
    prompt.prompt = '(hbnb) '
    prompt.cmdloop()
