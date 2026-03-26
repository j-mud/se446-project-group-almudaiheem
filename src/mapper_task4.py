import sys

for line in sys.stdin:
    line = line.strip()
    fields = line.split(',')

    if fields[0] == 'ID':
        continue

    if len(fields) > 2:
        date_str = fields[2].strip()
        try:
            year = date_str.split('/')[2].split(' ')[0]
            print(f'{year}\t1')
        except IndexError:
            continue
