# CSV converter

+ [Manual converter](#manual-converter)
+ [Converter with import](#converter-with-import)
+ [Unite tests](#unite-tests)

## Manual converter
```python
def read_file(file_path):
    f = open(file_path, encoding='utf-8')
    data = f.readlines()
    f.close()
    return data


def prepare_data(data):
    return data[0], data[1:]


def convert_row_to_pretty_json(keys, row):
    values = row.strip().split(',')
    keys = keys.strip().split(',')
    return dict(zip(keys, values))


def convert_csv_to_json(keys, data):
    res = [convert_row_to_pretty_json(keys, row) for row in data]
    return str(res).replace('\'', '\"')


def write_file(file_path, data):
    file_output = open(file_path, mode='w', encoding='utf-8')
    file_output.write(data)
    file_output.close()
    return 'Done!'


def main():
    raw_data = read_file('input.csv')
    keys, prepared_data = prepare_data(raw_data)
    res = convert_csv_to_json(keys, prepared_data)
    print(write_file('out.json', res))


if __name__ == '__main__':
    main()
```

## Converter with import
Difference from Manual converter in ```def convert_csv_to_json()```
```python
import json
...
def convert_csv_to_json(keys, data):
    lst = [convert_row_to_pretty_json(keys, row) for row in data]
    return json.dumps(lst)
...
```

## Unite tests
```python
import unittest
import csv_converter as c


class MyTestCase(unittest.TestCase):
    def test_read_file(self):
        res = c.read_file('input.csv')
        lst = 'id,name,birth,salary,department\n'
        self.assertEqual(res[0], lst)

    def test_prepare_data(self):
        raw_data = c.read_file('input.csv')
        keys, prepared_data = c.prepare_data(raw_data)

        self.assertEqual(type(keys), str)
        self.assertEqual(type(prepared_data), list)

    def test_convert_csv_to_json(self):
        raw_data = c.read_file('input.csv')
        keys, prepared_data = c.prepare_data(raw_data)
        res = c.convert_csv_to_json(keys, prepared_data)

        self.assertEqual(type(res), str)


if __name__ == '__main__':
    unittest.main()
```
