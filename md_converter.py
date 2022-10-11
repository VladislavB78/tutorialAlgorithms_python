def py_md_convert(file):
    file_py = open(file, encoding='UTF-8')
    txt = file_py.read()
    file_py.close()

    s = txt.split('# ---end---')

    title, description = '', ''
    for el in s[0].split('\n'):
        if el.startswith('# title'):
            title = el.strip().split('# title ')[1]
        elif el.startswith('# description'):
            description = el.strip().split('# description ')[1]

    file_txt = open('out.txt', mode='w', encoding='UTF-8')

    file_txt.write('+ [{}](#{})'.format(title, title.lower().replace(' ', '-')) + '\n\n')

    file_txt.write('## ' + title + '\n\n')
    file_txt.write(description + '\n\n')

    file_txt.write('```python' + s[1] + '```')

    file_txt.close()

    return 'Done!'


# Executing md converter
file = 'merge.py'
try:
    print(py_md_convert(file))
except OSError:
    print('{} not found!'.format(file))
