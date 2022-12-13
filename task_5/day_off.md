# Hour income calculation

+ [Hour income calculation](#hour-income-calculation)
+ [Tests](#tests)
<!---split here-->

## Calculator

Hour income calculation based on year, month and salary.

```python
import requests
import json
from enum import Enum


class APIRequest:

    def __init__(self, year, month):
        self.year = year
        self.month = month

    def get_response(self):
        url = f'https://isdayoff.ru/api/getdata?year={self.year}&month={self.month}'
        response = requests.get(url=url)
        if response.status_code == 200:
            return response.text
        return None


class Calculator:
    WORKING_DAY_TAG = '0'

    def __init__(self, input_json):
        self.input_json = input_json
        self.year = input_json['year']
        self.month = Months(input_json['month']).value
        self.salary = input_json['salary']
        self.hours = input_json['hours']
        self.hour_income = None

    def working_days(self):
        request = APIRequest(self.year, self.month)
        res = request.get_response()
        if res is not None:
            return res.count(self.WORKING_DAY_TAG)
        return None

    def calculate_hour_income(self):
        days = self.working_days()
        if days is None:
            return None
        self.hour_income = round(self.salary / days / self.hours, 2)

        self.input_json.update({'hour_income': self.hour_income})
        return self.input_json


class Months(Enum):
    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12

    DEFAULT = 99

    @classmethod
    def _missing_(cls, value):
        value = value.upper()
        for member in cls:
            if member.name == value:
                return member
        return cls.DEFAULT


def main():
    input_json = '{"year": 2022, "month": "NOVEMBER", "salary": 120000, "hours": 8}'
    calc = Calculator(json.loads(input_json))
    ans = calc.calculate_hour_income()
    print(ans)
```

## Tests

Testing APIRequest and Calculations

```python
import unittest
import json
from day_off import APIRequest, Calculator


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


class TestCalculator(unittest.TestCase):

    def test_working_days(self):
        input_json = '{"year": 2022, "month": "NOVEMBER", "salary": 120000, "hours": 8}'
        expected = Calculator(json.loads(input_json)).working_days()
        self.assertEqual(expected, 21)

        input_json = '{"year": 2022, "month": "99", "salary": 120000, "hours": 8}'
        expected = Calculator(json.loads(input_json)).working_days()
        self.assertEqual(expected, None)

    def test_calculate_hour_income(self):
        input_json = '{"year": 2022, "month": "NOVEMBER", "salary": 120000, "hours": 8}'
        expected = Calculator(json.loads(input_json)).calculate_hour_income()
        actual = {'year': 2022, 'month': 'NOVEMBER', 'salary': 120000, 'hours': 8, 'hour_income': 714.29}
        self.assertEqual(expected, actual)

        input_json = '{"year": 2022, "month": "99", "salary": 120000, "hours": 8}'
        expected = Calculator(json.loads(input_json)).calculate_hour_income()
        self.assertEqual(expected, None)


if __name__ == '__main__':
    unittest.main()
```
