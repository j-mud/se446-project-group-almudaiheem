import sys

for line in sys.stdin:
    line = line.strip()
    fields = line.split(',')

    if fields[0] == 'ID':
        continue

    if len(fields) > 5:
        crime_type = fields[5].strip()
        print(f"{crime_type}\t1")
