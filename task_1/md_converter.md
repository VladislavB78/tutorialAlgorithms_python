## Converter
```python
from os.path import exists

INPUT_CODE_DELIMITER = '# ---end---'
INPUT_MD_DELIMITER = '<!---split here-->'
OUTPUT_FILE_NAME = 'out.md'


def is_file_exists(file_name):
    try:
        open(file_name).close()
    except FileNotFoundError:
        return False
    else:
        return True


def read_file(file_name):
    file_input = open(file_name, encoding='UTF-8')
    data = file_input.read()
    file_input.close()

    return data


def md_convert(data):
    titles, source_code = data.split(INPUT_CODE_DELIMITER)
    title, description = prepare_md_titles(data)
    result_md = prepare_md_format(title, description, source_code)

    return result_md


def prepare_md_titles(data):
    title, description = '', ''
    for el in data.split('\n'):
        if el.startswith('# title'):
            title = el.strip().lstrip('# title ')
        elif el.startswith('# description'):
            description = el.strip().lstrip('# description ')

    return title, description


def prepare_md_format(title, description, source_code):
    md_link = '+ [{}](#{})'.format(title, '-'.join(title.lower().split()))

    template_new = """{}
{}

## {}

{}

```python{}```"""

    template_append = """

## {}

{}

```python{}```"""

    template_merge = """{}
{}

{}"""

    if exists(OUTPUT_FILE_NAME):
        links, sources = read_file(OUTPUT_FILE_NAME).split(INPUT_MD_DELIMITER)
        links += md_link
        sources += template_append.format(title, description, source_code)

        return template_merge.format(links, INPUT_MD_DELIMITER, sources.lstrip('\n'))
    else:
        return template_new.format(md_link, INPUT_MD_DELIMITER, title, description, source_code)


def write_file(file_name, data):
    file_output = open(file_name, mode='w', encoding='UTF-8')
    file_output.write(data)
    file_output.close()

    return 'Done!'


def start_converter(file_path):
    data = read_file(file_path)
    result = md_convert(data)
    print(write_file(OUTPUT_FILE_NAME, result))


if __name__ == '__main__':
    start_converter('src/compress.py')
```
