#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    NULL_not_found.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pollivie <plgol.perso@gmail.com>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/04/22 15:44:57 by pollivie          #+#    #+#              #
#    Updated: 2025/04/22 15:44:57 by pollivie         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def NULL_not_found(object: any) -> int:
    if isinstance(object, type(None)):
        print(f"Nothing: {object} {type(object)}")
    elif isinstance(object, float):
        print(f"Cheese: {object} {type(object)}")
    elif isinstance(object, bool):
        print(f"Fake: {object} {type(object)}")
    elif isinstance(object, int):
        print(f"Zero: {object} {type(object)}")
    elif isinstance(object, str):
        if len(str(object)) == 0:
            print(f"Empty: {type(object)}")
        else:
            print("Type not Found")
            return 1
    else:
        print("Type not Found")
        return 1
    return 0
