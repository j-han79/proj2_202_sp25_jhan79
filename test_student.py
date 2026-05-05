import unittest
from proj2 import *

class TestProj2(unittest.TestCase):

    def test_parse_float_empty(self):
        self.assertEqual(parse_float(""), None)
    def test_parse_float_number(self):
        self.assertEqual(parse_float("1.2"), 1.2)
    def test_parse_row(self):
        row = parse_row(["Japan", "2020", "514.36", "4.12", "989.57", "7.901", "1014.06", "8.096"])
        self.assertEqual(row.country, "Japan")
        self.assertEqual(row.year, 2020)
        self.assertEqual(row.electricity_and_heat_co2_emissions, 514.36)
        self.assertEqual(row.electricity_and_heat_co2_emissions_per_capita, 4.12)
        self.assertEqual(row.energy_co2_emissions, 989.57)
        self.assertEqual(row.energy_co2_emissions_per_capita, 7.901)
        self.assertEqual(row.total_co2_emissions_excluding_lucf, 1014.06)
        self.assertEqual(row.total_co2_emissions_excluding_lucf_per_capita, 8.096)

    def test_listlen_empty(self):
        self.assertEqual(listlen(None), 0)

    def test_listlen_three_nodes(self):
        row1 = Row("A", 2013, 1.2, None, 3.4, None, 5.6, None)
        row2 = Row("B", 2000, 1.5, None, 8.4, None, 2.6, None)
        row3 = Row("C", 2015, 6.0, None, 5.4, None, 8.6, None)
        data = Node(row1, Node(row2, Node(row3, None)))
        self.assertEqual(listlen(data), 3)

    def test_filter_country_equal(self):
        row1 = Row("United States", 2019, 1.0, None, 2.0, None, 3.0, None)
        row2 = Row("Canada", 2019, 10.0, None, 5.0, None, 6.0, None)

        data = Node(row1, Node(row2, None))
        result = filter_rows(
            data,
            "electricity_and_heat_co2_emissions",
            "greater_than",
            5.0
        )
        self.assertEqual(listlen(result), 1)
        self.assertEqual(result.value.country, "Canada")

    def test_filter_skips_none(self):
        row1 = Row("United States", 2019, None, None, 2.0, None, 3.0, None)
        row2 = Row("Canada", 2019, 10.0, None, 5.0, None, 6.0, None)
        data = Node(row1, Node(row2, None))
        result = filter_rows(
            data,
            "electricity_and_heat_co2_emissions",
            "greater_than",
            5.0
        )
        self.assertEqual(listlen(result), 1)
        self.assertEqual(result.value.country, "Canada")
    def test_read_csv(self):
        data = read_csv_lines("test_data.csv")
        self.assertEqual(listlen(data), 5)

if __name__ == '__main__':
    unittest.main()
