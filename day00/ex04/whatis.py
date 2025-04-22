#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whatis.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pollivie <plgol.perso@gmail.com>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/04/22 16:06:22 by pollivie          #+#    #+#              #
#    Updated: 2025/04/22 16:06:22 by pollivie         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys as sys


def isEvenOrOddStr(number: any) -> str:
    if abs(int(number)) & 1 == 0:
        print("I'm Even")
    else:
        print("I'm Odd")


def main() -> int:
    argc: int = len(sys.argv)

    if argc == 1:
        return 0
    if argc > 2:
        print("AssertionError: more than one argument is provided")
        return 1

    try:
        number: int = int(sys.argv[1])
        isEvenOrOddStr(number=number)
    except Exception:
        print("AssertionError: argument is not an integer")
        return 1

    return 0


if __name__ == "__main__":
    main()
