#!/usr/bin/env python3
"""This module defines the HBNBCommand class."""
import cmd
from models import storage
from models.base_model import BaseModel
from shlex import split
import sys

class HBNBCommand(cmd.Cmd):
    """Command interpreter class for HBNB console."""

    # Existing methods unchanged...

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print its id."""
        args = split(arg)
        if not args:
            print("** class name missing **")
        else:
            try:
                new_instance = eval(args[0])()
                new_instance.save()
                print(new_instance.id)
            except NameError:
                print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        args = split(arg)
        if not args or len(args) == 1:
            print("** class name missing **")
        else:
            try:
                instance_key = args[0] + "." + args[1]
                instance = storage.all().get(instance_key)
                if instance:
                    print(instance)
                else:
                    print("** no instance found **")
            except NameError:
                print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = split(arg)
        if not args or len(args) == 1:
            print("** class doesn't exist **")
        else:
            try:
                instance_key = args[0] + "." + args[1]
                if instance_key in storage.all():
                    del storage.all()[instance_key]
                    storage.save()
                else:
                    print("** instance id missing **")
            except NameError:
                print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representations of instances."""
        args = split(arg)
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
        args = split(arg)
        if not args or len(args) < 3:
            print("** attribute name missing **")
        else:
            try:
                instance_key = args[0] + "." + args[1]
                instance = storage.all().get(instance_key)

                if not instance:
                    print("** no instance found **")
                    return

                if len(args) < 4:
                    print("** attribute name missing **")
                    return

                if len(args) < 5:
                    print("** value missing **")
                    return

                attribute_name = args[3]
                attribute_value = args[4]

                if hasattr(instance, attribute_name) and attribute_name not in ["id", "created_at", "updated_at"]:
                    attr_type = type(getattr(instance, attribute_name))
                    setattr(instance, attribute_name, attr_type(attribute_value))
                    instance.save()
                else:
                    print("** attribute doesn't exist **")

            except NameError:
                print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
