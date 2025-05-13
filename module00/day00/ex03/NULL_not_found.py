#!/usr/bin/env python3


def isNullInteger(object: any) -> bool:
    """Returns true if object is of type 'int' and is equal to '0'"""
    return isinstance(object, int) and object == 0


def isNullFloat(object: any) -> bool:
    """Returns true if object is of type 'float' and is equal to 'NaN'"""
    return isinstance(object, float) and object != object


def isNullString(object: any) -> bool:
    """Returns true if object is of type 'str' and of length '0'"""
    return isinstance(object, str) and len(str(object)) == 0


def isNullBool(object: any) -> bool:
    """Returns true if object is of type 'bool' and is equal to 'False'"""
    return isinstance(object, bool) and not object


def isAnyNone(object: any) -> bool:
    """Returns true if object is of type 'NoneType'"""
    return object is None


def NULL_not_found(object: any) -> int:
    """Returns 1 if 'object' is not considered a 'NULL' type else 1"""
    if isAnyNone(object):
        print(f"Nothing: None {type(object)}")
    elif isNullFloat(object):
        print(f"Cheese: {object} {type(object)}")
    elif isNullBool(object):
        print(f"Fake: {object} {type(object)}")
    elif isNullInteger(object):
        print(f"Zero: {object} {type(object)}")
    elif isNullString(object):
        print(f"Empty: {type(object)}")
    else:
        print("Type not Found")
        return 1
    return 0


# def main() -> None:
#     """Main"""
#     Nothing = None
#     Garlic = float("NaN")
#     Zero = 0
#     Empty = ""
#     Fake = False
#     NULL_not_found(Nothing)
#     NULL_not_found(Garlic)
#     NULL_not_found(Zero)
#     NULL_not_found(Empty)
#     NULL_not_found(Fake)
#     print(NULL_not_found("Brian"))


# if __name__ == "__main__":
#     main()
