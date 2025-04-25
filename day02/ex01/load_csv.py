#!/usr/bin/env python

import pandas as pd
import pathlib as pl


def load(path: str) -> pd.DataFrame:
    path = pl.Path(path)
    if not path.exists() or not path.is_file():
        raise ValueError("InvalidPath")
    return pd.DataFrame(pd.read_csv(path))
