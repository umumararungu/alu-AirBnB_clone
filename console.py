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

    def quit_(self, arg):
        """
        """
        return True
    
    def EOF_(self,arg):
        """
        """
        print()
        return True
    def help_(self,arg):
        """
        """
        print("Quit to exit program")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
