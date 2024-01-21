#!/usr/bin/env python3
"""This module defines the HBNBCommand class."""
import cmd
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import shlex
import sys

class HBNBCommand(cmd.Cmd):
    """Command interpreter class for HBNB console."""
    
    valid_classes = ["BaseModel"]

    def do_quit(self, arg):
        """
        """
        return True
    
    def help_quit(self, arg):
        """
        """
        print("Quit to exit program")
        
    def do_EOF(self, arg):
        """
        """
        print("")
        return True
    def emptyline(self,):
        """
        empty line
        """
        pass

    prompt = "(hbnb) "

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print its id."""
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
            
    def do_show(self, arg):
        """Prints the string representation of an instance."""
        args = shlex.split(arg)
        if not args or len(args) == 1:
            print("** instance id missing **")
        else:
            try:
                instance = storage.all()[args[0] + "." + args[1]]
                print(instance)
            except KeyError:
                print("** no instance found **")
            except NameError:
                print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = shlex.split(arg)
        if not args or len(args) == 1:
            print("** instance id missing **")
        else:
            try:
                instance_key = args[0] + "." + args[1]
                del storage.all()[instance_key]
                storage.save()
            except KeyError:
                print("** class doesn't exist **")
            except NameError:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representations of instances."""
        args = shlex.split(arg)
        obj_list = []
        if not args or len(args) == 1:
            for key, value in storage.all().items():
                obj_list.append(str(value))
            print(obj_list)
        else:
            try:
                for key, value in storage.all().items():
                    if key.split('.')[0] == args[0]:
                        obj_list.append(str(value))
                print(obj_list)
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = shlex.split(arg)
        if not args or len(args) == 1:
            print("** instance id missing **")
        else:
            try:
                instance_key = args[0] + "." + args[1]
                instance = storage.all()[instance_key]
                if len(args) == 2:
                    print("** attribute name missing **")
                    return
                if len(args) == 3:
                    print("** attribute name missing **")
                    return
                if len(args) == 4:
                    print("** value missing **")
                    return

                attribute_name = args[3]
                attribute_value = args[4]

                if hasattr(instance, attribute_name):
                    attr_type = type(getattr(instance, attribute_name))
                    setattr(instance, attribute_name, attr_type(attribute_value))
                    instance.save()
                else:
                    print("** attribute doesn't exist **")

            except KeyError:
                print("** no instance found **")
            except NameError:
                print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()

