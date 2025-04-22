#!/usr/bin/env python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    format_ft_time.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: pollivie <plgol.perso@gmail.com>           +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/04/22 15:10:05 by pollivie          #+#    #+#              #
#    Updated: 2025/04/22 15:10:05 by pollivie         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time as tm


def format_ft_time() -> str:
    epoch_second: float = tm.time()
    local_time: tm.struct_time = tm.localtime(epoch_second)
    intro_str: str = "Seconds since January 1, 1970:"
    outro_str: str = "in scientific notation"
    epoch_sec: str = tm.strftime(f"{epoch_second:,}")
    epoch_sci: str = tm.strftime(f"{epoch_second:.2e}")
    epoch_dat: str = tm.strftime("%b %d %Y", local_time)
    return format(f"{intro_str} {epoch_sec} or {epoch_sci} {outro_str}\n{epoch_dat}")


print(format_ft_time())
