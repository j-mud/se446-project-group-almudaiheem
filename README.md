# se446-project-group-almudaiheem
Repository for SE446 (Intro to Big Data) Term project.
Task 4: Year Trend Analysis

Goal:
Analyze how the total number of crimes changed over the years by extracting the year from the Date column (index 2) and counting crimes per year.

Mapper:
mapper_task4.py

Reducer:
reducer_sum.py

Command:
mapred streaming \
-files mapper_task4.py,reducer_sum.py \
-mapper 'python3 mapper_task4.py' \
-reducer 'python3 reducer_sum.py' \
-input /data/chicago_crimes.csv \
-output /user/fsad/project/m1/task4

Top 5 years by crime count:
2001    467301
2002    205267
2023    81461
2025    12710
2022    4678
