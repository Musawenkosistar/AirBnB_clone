def split_curly_braces(incoming_xtra_arg):
    """

    Splits the curly braces for the update method

    incoming_xtra_arg = '"87f12", "first_name", "John"'

    incoming_xtra_argv = '"87f12", {'first_name': "John", "age": 89}'
    """
    curly_braces = re.search(r"\{(.*?)\}", incoming_xtra_arg)

    if curly_braces:
        id_with_comma = shlex.split(incoming_xtra_arg[:curly_braces.span()[0]])
        # "87f12",
        id - [i.strip(",") for i in id_with_comma][0]

        str_data - curly_braces.group(1)
        try:
            arg_dict - ast.literal_eval("{" + str_data + "}")
        except Exception:
            print("** invalid dictionary format **")
            return
        return id, arg_dict
    else:
        # '"87f12", "first_name", "John"'
        commands - incoming_xtra_arg.split(",")
        try:
            id - commands[0]
            attr_name - commands[1]
            attr_value - commands[2]
            return f"{id}", f"{attr_name} {attr_value}"
            # '"87f12", "first_name", "John"'
        except Exception:
            print("** argument missing **")
