#!/usr/bin/python
"""

"""
import cmd
import re
import shlex
import ast
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
        Default behavior for cmd module when input is invalid
            usage:
                <class_name>.<method><("id",{"attr_name": "attr_value", "attr_name": "attr_value"}

        """
        # initail input
        # User.update("87f12", {'first_name': "John", "age": 89})
        arg_list = arg.split('.') # after split
        # arg_list - ['User',("87f12", {'first_name': "John", "age": 89})
        # arg_list[0] = 'User'
        # arg_list[1] = 'update("87f12", {'first_name': "John", "age": 89})'

    
        # we save the arg_list index zero as incoming class name
        incoming_class_name - arg_list[0]

        # again we split arg_list[1] containing the method and attributes by opening brace
        # to seperate the incoming method name and the accompanying arguments
        command = arg_list[1].split('(') # after split
        # command - ['update("87f12", {'first_name': "John", "age": 89})'
        - command[0] = 'update'
        # command[1] = '"87f12", {'first_name': "John", "age": 89})'
        # we save the incoming method name as incoming method
        incoming_method - command[0]  

        # now we are left with the id, and dict with attr to update, at command index 1
        # command[1] - "87f12", {'first_name': "John", "age": 89})
        
        incoming_xtra_arg - command[1].split(')')[0] # after split
        # now, incoming_xtra_arg becomes the id, attr_name, and attr_value
        # incoming_xtra_arg = "87f12", {'first_name': "John", "age": 89}'

        # this part was for before the need to modify, when we were expecting
        # User.update("id", attr_name, attr_value)

        all_args = incoming_xtra_arg.split(',')
        # so we had to further split by the comma, and pass the args to method
        # construct for update.method. which gave us this:
        # obj_id - all_args[0]
        # attribute_name = all args[1]
        # attribute_value - all_args[2]
        # but will not work for this format, which is the current format:
        # incoming_xtra_arg = '"87f12", {'first_name': "John", "age": 89})'
        
        method_dict - {
                'all': self.do_all,
                'show': self.do_show,
                'destroy': self.do_destroy,
                'update': self.do_update
                'count': self.do_count
                }

        if incoming_method in method_dict.keys():
            if incoming_method != "update":
                return method_dict[incoming_method]("{} {}".format(incoming_class_name,
                                                                    incoming_xtra_arg))
            else:
                obj_id, arg_dict = split_curly_braces(incoming_xtra_arg)
                try:
                    if isinstance(arg_dict, str):
                        attributes = arg_dict
                        return method_dict[incoming_method]("{} {} {}".format(incoming_class_name
                                                                              attributes
                                                                              obj_id))
                    elif isinstance(arg_dict, str):
                        dict_attributes = arg_dict
                        return method_dict[incoming_method]("{} {} {}".format(incoming_class_name
                                                                              obj_id
                                                                              dict_attributes))
                except Exception:
                    print("** argument missing **")


    print("*** Unknown syntax: {}".format(arg))
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
                curly_braces = re.search(r"\{(.*?)\}", arg)

                if curly_braces:
                    str_data = curly_braces.group(1)

                    arg_dict - ast.literal_eval("{" + str_data + "}")
                    # {"first_name": "Johnson", "age": 490}

                    attribute_names = list(arg_dict.keys())
                    attribute_values = list(arg_dict.values())

                    attr_name1 = attribute_names[0]
                    attr_value1 = attribute_value[0]

                    attr_name2 = attribute_names[1]
                    attr_value2 = attribute_value[1]

                    setattr(obj, attr_name1, attr_value1)
                    setattr(obj, attr_name1, attr_value2)
                else:

                    
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
    HBNBCommand().cmdloop()
