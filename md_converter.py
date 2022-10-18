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


def write_file(file_name, data):
    file_output = open(file_name, mode='w', encoding='UTF-8')
    file_output.write(data)
    file_output.close()

    return 'Done!'


def prepare_md_titles(data):
    title, description = '', ''
    for el in data.split('\n'):
        if el.startswith('# title'):
            title = el.strip().lstrip('# title ')
        elif el.startswith('# description'):
            description = el.strip().lstrip('# description ')

    return title, description


def prepare_md_format(title, description, source_code):
    # md_link = '-'.join(title.lower().split())
    md_link = '+ [{}](#{})'.format(title, '-'.join(title.lower().split()))

    template_new = """{}
<!---split here-->

## {}

{}

```python{}```"""

    template_append = """

## {}

{}

```python{}```"""

    template_merge = """{}
<!---split here-->

{}"""

    if is_file_exists(OUTPUT_FILE_NAME):
        links, sources = read_file(OUTPUT_FILE_NAME).split(INPUT_MD_DELIMITER)
        links += md_link
        sources += template_append.format(title, description, source_code)

        return template_merge.format(links, sources.lstrip('\n'))
    else:
        return template_new.format(md_link, title, description, source_code)


def md_convert(data):
    titles, source_code = data.split(INPUT_CODE_DELIMITER)
    title, description = prepare_md_titles(data)
    result_md = prepare_md_format(title, description, source_code)

    return result_md


def main():
    file_name = 'compress.py'
    data = read_file(file_name)
    result = md_convert(data)
    print(write_file(OUTPUT_FILE_NAME, result))


if __name__ == '__main__':
    main()
