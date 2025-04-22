#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    find_ft_type.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pollivie <plgol.perso@gmail.com>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/04/22 15:11:27 by pollivie          #+#    #+#              #
#    Updated: 2025/04/22 15:11:27 by pollivie         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


def all_thing_is_obj(object: any) -> int:
    if isinstance(object, str):
        print(f"{object} is in the kitchen : {type(object)}")
    elif isinstance(object, int):
        print("Type not found")
    else:
        print(f"{type(object).__name__.capitalize()} : {type(object)}")

    return 42
