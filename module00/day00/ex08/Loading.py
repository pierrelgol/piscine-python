#!/usr/bin/env python


def ft_tqdm(lst: range) -> None:
    """Tqdm imitation"""
    total: int = 0
    try:
        total = len(lst)
    except TypeError:
        raise ValueError("invalid range")

    def printProgress(index: int) -> None:
        """inner print function"""
        percent: float = index / total
        progress = int(80 * percent)
        if index == total:
            bar = "=" * 79 + ">"
        else:
            bar = "=" * max(0, progress - 1) + ">" + " " * (80 - progress)
        print(
            f"{int(round(percent * 100)):3}% |[{bar}]| {index}/{total}",
            end="\r",
            flush=True,
        )
        return

    for i, item in enumerate(lst):
        yield item
        printProgress(i + 1)
    print()
