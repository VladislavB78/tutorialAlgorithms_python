+ [Hour income calculation](#hour-income-calculation)
+ [Tests](#tests)
<!---split here-->

## Hour income calculation

Hour income calculation based on year, month and salary.

```python
import requests


class APIRequest:

    def __init__(self, year: int, month: int):
        self.year = year
        self.month = month

    def get_response(self):
        url = f'https://isdayoff.ru/api/getdata?year={self.year}&month={self.month}'
        response = requests.get(url=url)
        if response.status_code == 200:
            return response.text
        return None


class Calculations:

    WORKING_DAY_TAG = '0'

    def __init__(self, year: int, month: int, salary: int, working_hours: int = 8):
        self.year = year
        self.month = month
        self.salary = salary
        self.working_hours = working_hours
        self.hour_income = None

    def working_days(self):
        request = APIRequest(self.year, self.month)
        res = request.get_response()
        if res is not None:
            return res.count(self.WORKING_DAY_TAG)
        return None

    def calculate_hour_income(self):
        wd = self.working_days()
        if wd is None:
            return None
        self.hour_income = round(self.salary / wd / self.working_hours, 3)
        return self.hour_income


def main():
    calc = Calculations(2022, 11, 120000)
    print(calc.calculate_hour_income())


if __name__ == '__main__':
    main()
```

## Tests

Testing APIRequest and Calculations

```python
import unittest
from day_off import APIRequest, Calculations


class TestAPIRequest(unittest.TestCase):

    def test_get_response(self):
        request = APIRequest(2022, 11)
        response = '000111000001100000110000011000'
        self.assertEqual(request.get_response(), response)

        request = APIRequest(1700, 1)
        response = '0000000000000000000000000000000'
        self.assertEqual(request.get_response(), response)

        request = APIRequest(2022, 99)
        response = None
        self.assertEqual(request.get_response(), response)


class TestCalculations(unittest.TestCase):

    def test_working_days(self):
        calc = Calculations(2022, 11, 120000)
        self.assertEqual(calc.working_days(), 21)

        calc = Calculations(2022, 99, 120000)
        self.assertEqual(calc.working_days(), None)

    def test_calculate_hour_income(self):
        calc = Calculations(2022, 11, 120000)
        self.assertEqual(calc.calculate_hour_income(), 714.286)

        calc = Calculations(2022, 99, 120000)
        self.assertEqual(calc.calculate_hour_income(), None)


if __name__ == '__main__':
    unittest.main()
```
