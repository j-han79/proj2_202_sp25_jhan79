from __future__ import annotations
import sys
import csv
from typing import *
from dataclasses import dataclass
import unittest
import math

sys.setrecursionlimit(10_000)

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

def parse_float(value: str) -> Optional[float]:
    """Covert string to float, or return None if string is empty"""
    if value == "":
        return None
    return float(value)

def parse_row(fields: list[str]) -> Row:
    """Convert a list of CSV string values into a row object with types"""
    return Row(
        country=fields[0],
        year=int(fields[1]),
        electricity_and_heat_co2_emissions=parse_float(fields[2]),
        electricity_and_heat_co2_emissions_per_capita=parse_float(fields[3]),
        energy_co2_emissions=parse_float(fields[4]),
        energy_co2_emissions_per_capita=parse_float(fields[5]),
        total_co2_emissions_excluding_lucf=parse_float(fields[6]),
        total_co2_emissions_excluding_lucf_per_capita=parse_float(fields[7]),
    )

def build_list(rows: list[list[str]], index: int) -> Optional[Node]:
    """Recursively build a linked list of row objects from a list of CSV rows."""
    if index >= len(rows):
        return None
    return Node(
        value = parse_row(rows[index]),
        next = build_list(rows, index + 1)
    )

def read_csv_lines(filename: str) -> Optional[Node]:
    """Read a CSV file and return its data rows as a linked list of row nodes."""
    with open(filename, newline="") as file:
        reader = csv.reader(file)
        rows = list(reader)

    if len(rows) <= 1:
        return None

    data_rows = rows[1:]
    return build_list(data_rows, 0)

def listlen(data: Optional[Node]) -> int:
    """Return the number of nodes in the linked list."""
    if data is None:
        return 0
    return 1 + listlen(data.next)

def filter_rows(
        data: Optional[Node],
        field_name: str,
        comparison: str,
        value: Union[str, int, float]
) -> Optional[Node]:
    """Return a new linked list containing rows that match given field, comparison, and value."""
    if data is None:
        return None
    row_value = getattr(data.value, field_name)
    rest = filter_rows(data.next, field_name, comparison, value)
    if row_value is None:
        return rest
    keep = False
    if field_name == "country":
        if comparison == "equal":
            keep = row_value == value
    else:
        if comparison == "less_than":
            keep = row_value < value
        elif comparison == "greater_than":
            keep = row_value > value
        elif comparison == "equal":
            keep = row_value == value
    if keep:
        return Node(data.value, rest)
    return rest
