#!/usr/bin/python3
"""
Console module for AirBnB clone
"""

import cmd
import shlex
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print its id."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
        else:
            class_name = args[0]
            if class_name not in storage.classes:
                print("** class doesn't exist **")
            else:
                new_instance = storage.classes[class_name]()
                new_instance.save()
                print(new_instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance."""
        args = shlex.split(arg)
        if not args or len(args) == 1:
            print("** class name missing **" if not args else "** instance id missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            if class_name not in storage.classes:
                print("** class doesn't exist **")
            else:
                key = "{}.{}".format(class_name, instance_id)
                obj = storage.all().get(key)
                if obj:
                    print(obj)
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        args = shlex.split(arg)
        if not args or len(args) == 1:
            print("** class name missing **" if not args else "** instance id missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            if class_name not in storage.classes:
                print("** class doesn't exist **")
            else:
                key = "{}.{}".format(class_name, instance_id)
                obj = storage.all().get(key)
                if obj:
                    del storage.all()[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """Print all string representations of instances based on the class name."""
        args = shlex.split(arg)
        if not args:
            objs = storage.all()
        else:
            class_name = args[0]
            if class_name not in storage.classes:
                print("** class doesn't exist **")
                return
            objs = {k: v for k, v in storage.all().items() if class_name in k}

        print([str(obj) for obj in objs.values()])

    def do_update(self, arg):
        """Update an instance based on the class name and id."""
        args = shlex.split(arg)
        if not args or len(args) == 1:
            print("** class name missing **" if not args else "** instance id missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            if class_name not in storage.classes:
                print("** class doesn't exist **")
            else:
                key = "{}.{}".format(class_name, instance_id)
                obj = storage.all().get(key)
                if obj:
                    if len(args) < 4:
                        print("** attribute name missing **")
                    else:
                        attr_name = args[2]
                        if len(args) < 5:
                            print("** value missing **")
                        else:
                            value = args[3]
                            setattr(obj, attr_name, value)
                            obj.save()
                else:
                    print("** no instance found **")

    def do_quit(self, arg):
        """Quit the command interpreter."""
        return True

    def do_EOF(self, arg):
        """Handle end of file."""
        print()
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
