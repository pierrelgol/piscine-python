#!/usr/bin/env python


def count_in_list(items: list[str] = [], item: str = "") -> int:
    return [i for i in items if i == item].count(item)
