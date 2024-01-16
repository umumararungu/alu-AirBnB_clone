#!/usr/bin/python3
"""
console file
"""
import cmd

class HBNBCommand(cmd.Cmd):
    """
    Cmd
    """
    prompt = "(hbnb)"

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
        print()
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
