#!/usr/bin/env python


def ft_tqdm(lst: range) -> None:
    """Tqdm imitation"""
    total: int = 0
    try:
        total = len(lst)
    except TypeError:
        raise ValueError("invalid range")

    def printProgress(index: int) -> None:
        percent: float = index / total
        progress_len = int(80 * percent)
        bar = "=" * progress_len + " " * (80 - progress_len)
        print(
            f"{int(round(percent * 100))}% |[{bar}]| {index}/{total}",
            end="\r",
            flush=True,
        )
        return

    for i, item in enumerate(lst):
        yield item
        printProgress(i + 1)
    print()
