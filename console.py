#!/usr/bin/python
"""

"""
import cmd
import re
import shlex
from models.base model import BaseModel
from models.user import User
from models import storage
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City


class HBNBCommand(cmd.Cmd):
    """
    
    """
    prompt = "(hbnb)"
    valid_classes = ["BaseModel", "User", "Amenity"
                     "Place", "Review", "State", "City"]
    



    def emptyline(self):
        """
        
        """
        pass

    def do_EOF(self, line):
        """

        """
        return True

    def do_quit(self, arg):
        """

        """
        return True
    
    def do_create(self, arg):
        """

        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing**")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(f"{commands[0]}()")
            storage.save()
            print(new_instance.id)
    
    def do_show(self, arg):
        """

        """
        cammands = shlex.split(arg) # show User "12w-241"

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print ("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()

            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")


    def do_destroy(self, arg):
        """

        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(commands) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(commands[0], commands[1])
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")


    def do_all(self, arg):
        """

        """

    objects = storage.all()

    commands = shlex.split(arg)

    if len(commands) == 0:
        for key, value in objects.items():
            print(str(value))
    elif commands[0] not in self.valid_classes:
        print("** class doesn't exist **")
    else:
        for key, value in objects.items():
            if key.split('.')[0] == commands[0]:
                print(str(value))

    def default(self, arg):
        """

        """
        arg_list = arg.split('.') #User.show("12w-241') output: ['User', 'show("12w-241")']
    
        # arg_list[0] = 'User'
        # arg_list[1] = 'show("12w-241")'
        incoming_class_name - arg_list[0]

        command = arg_list[1].split('(')
        # command[0] = 'show'
        # command[1] = '"12w-241")'

        incoming_method - command[0]  # 'show'
        
        incoming_xtra_arg - command[1].split(')')[0]  # ['"12w-241"', '']

    
        method_dict - {
                'all': self.do_all,
                'show': self.do_show,
                'destroy': self.do_destroy,
                'update': self.do_update
                'count': self.do_count

        }

        if incoming_method in method_dict.keys():
            return method_dict[incoming_method]("{}.{}".format(incoming_class_name,
                incoming_xtra_arg))

    print("*** Unknown syntax: ()".format(arg))
    return False

        def do_count(self, arg):
            """

            """
            objects = storage.all()

            # Use.count() City.count()
            # count User or count City

            commands = shlex.split(arg)  # ['User']
            # commands[0] = 'User'
            if arg:
                incoming_class_name = commands[0]


            count = 0

            if incoming_class_name in self.valid_classes:
                for obj in objects.values():
                    if obj.__class__.__name__== incoming_class_name:
                        count +- 1
                    print(count)
                else:
                    print("** invalid class name **")
            else:
                print("** class name missing **")
             


        def do_update(self, arg):
        """

        """
        commands = shlex.split(arg)

        if len(commands) == 0:
            print("** class name missing **")
        elif commands[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif commands[0] < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()

            key = "{}.{}".format(commands[0], commands[1])
            if key not in objects:
                print("** no instance found **")
            elif len(commands) < 3:
                print("** attribute name missing **")
            elif len(commands) ,< 4:
                print("** value missing **")
            else:
                obj = objects[key]

                attr_name = commands[2]
                attr_value = commands[3]

                try:
                    attr_value = eva;(attr_value)
                except Exception:
                    pass
                setatrr(obj, attr_name, attr_value)

                obj.save()
    def help_quit(self, arg):
        """

        """
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """

        """
        print()
        return True

if __name__ == "__main__":
    HBNBCommand().cm
