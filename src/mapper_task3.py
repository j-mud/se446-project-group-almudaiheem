import sys

for line in sys.stdin:
    line = line.strip()
    fields = line.split(',')

    if fields[0] == 'ID':
        continue

    if len(fields) > 7:
        location = fields[7].strip()
        print(f'{location}\t1')
        
