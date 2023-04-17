import unittest
from datetime import datetime, timedelta
import date_increment


class TestDateIncrement(unittest.TestCase):

    def _check_data_increment(self, value):
        initial_date = datetime.strptime(value[0], "%d.%m.%Y")
        expected_date = initial_date + timedelta(days=value[1])
        expected_date_string = expected_date.strftime("%d.%m.%Y")
        actual_date = date_increment.date_increment(value[0], value[1])
        self.assertEqual(expected_date_string, actual_date)

    def test_date_increment_basic(self):
        self._check_data_increment(("01.01.2023", 10))

    def test_date_increment_month_change(self):
        self._check_data_increment(("21.01.2023", 15))

    def test_date_increment_year_change(self):
        self._check_data_increment(("31.12.2023", 1))

    def test_date_increment_leap_year(self):
        self._check_data_increment(("25.02.2024", 5))

    def test_date_increment_leap_year_400(self):
        self._check_data_increment(("28.02.1599", 366))

    def test_date_increment_not_leap_year_400(self):
        self._check_data_increment(("28.02.1899", 366))

    def test_date_increment_0_days(self):
        self._check_data_increment(("01.07.2011", 0))

    def test_date_increment_many_days(self):
        self._check_data_increment(("11.11.1918", 40000))
