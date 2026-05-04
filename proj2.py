import csv
import math
from dataclasses import dataclass
from typing import *


# Put your data definitions first!
@dataclass(frozen=True)
class Row:
    country: str
    year: int
    electricity_and_heat_co2_emissions: Optional[float]
    electricity_and_heat_co2_emissions_per_capita: Optional[float]
    energy_co2_emissions: Optional[float]
    energy_co2_emissions_per_capita: Optional[float]
    total_co2_emissions_excluding_lucf: Optional[float]
    total_co2_emissions_excluding_lucf_per_capita: Optional[float]
@dataclass(frozen=True)
class Node:
    value: Row
    next: Optional[Node]
# ...

# Then your functions.
def parse_float(value: str) -> Optional[float]:
    if value == "":
        return None
    return float(value)
# ...
