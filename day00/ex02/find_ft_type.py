#!/usr/bin/env python3


def isNumber(object: any) -> bool:
    """This function returns true if 'object' is of type 'int | float'"""
    return isinstance(object, int | float)


def isString(object: any) -> bool:
    """This function returns true if 'object' is of type 'str'"""
    return isinstance(object, str)


def getCapitalizedName(object: any) -> str:
    """This function returns the capitalized name of any given type"""
    return type(object).__name__.capitalize()


def all_thing_is_obj(object: any) -> int:
    """This function display 'object' differently depending on it's type"""
    if isNumber(object):
        print("Type not found")
    elif isString(object):
        print(f"{object} is in the kitchen : {type(object)}")
    else:
        print(f"{getCapitalizedName(object)} : {type(object)}")
    return 42
