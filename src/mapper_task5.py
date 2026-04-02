import sys

for line in sys.stdin:
    line = line.strip()
    fields = line.split(',')

    if fields[0] == 'ID':
        continue

    if len(fields) > 8:
        arrested = fields[8].strip()
        print(f'{arrested}\t1')