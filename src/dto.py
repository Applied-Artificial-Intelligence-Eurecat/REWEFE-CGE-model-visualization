from dataclasses import dataclass

import pandas as pd


@dataclass
class Scenario:
    name: str
    description: str
    df: pd.DataFrame
