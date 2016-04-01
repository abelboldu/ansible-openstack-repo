def do_capitalize(arg): 
    """
    Capitalize a value. The first character will be uppercase, all others
    lowercase.
    """
    return arg.capitalize()


class FilterModule(object): 
    def filters(self): 
        return {'do_capitalize': do_capitalize} 
