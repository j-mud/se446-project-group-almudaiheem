# SE446-Project-Group-Almudaiheem
Repository for SE446 (Intro to Big Data) Term project.

# SE446 Project Milestone 1: Chicago Crime Analytics with MapReduce

## Group Name
SE446-Project-Group-Almudaiheem

## Team Members

| Name | Student ID | Role / Task |
|---|---:|---|
| Fjr Sad | 231722 | Task 4 — Year Trend Analysis |
| [Member 2 Name] | [ID] | Task 2 — Crime Type Distribution |
| [Member 3 Name] | [ID] | Task 3 — Location Hotspots |
| [Member 4 Name] | [ID] | Task 5 — Arrest Rate |
| [Member 1 Name] | [ID] | Task 1 — Repo Setup, Shared Reducer |

## Summary

This project uses Hadoop MapReduce to analyze the Chicago crime dataset and answer key questions about crime patterns. We implemented separate mappers for crime type distribution, location hotspots, year-based crime trends, and arrest analysis, while reusing a shared reducer to aggregate counts.

Each task was tested locally and then executed on the Hadoop cluster using `mapred streaming`. The final outputs help summarize what crimes are most common, where they happen most often, how crime volume changes over time, and what percentage of crimes result in arrest.

---

## Task 2: Crime Type Distribution

### Research Question
What are the most common types of crimes in Chicago?

### Command
```bash
mapred streaming \
-files mapper_task2.py,reducer_sum.py \
-mapper 'python3 mapper_task2.py' \
-reducer 'python3 reducer_sum.py' \
-input /data/chicago_crimes.csv \
-output /user/[your_id]/project/m1/task2
```

### Top 5 Results
```text
[Paste top 5 lines from task 2 output here]
```

### Interpretation
[Write one sentence interpreting Task 2 results.]

### Execution Logs
```text
[Paste full terminal output for Task 2 here]
```

---

## Task 3: Location Hotspots

### Research Question
Where do most crimes occur?

### Command
```bash
mapred streaming \
-files mapper_task3.py,reducer_sum.py \
-mapper 'python3 mapper_task3.py' \
-reducer 'python3 reducer_sum.py' \
-input /data/chicago_crimes.csv \
-output /user/[your_id]/project/m1/task3
```

### Top 5 Results
```text
[Paste top 5 lines from task 3 output here]
```

### Interpretation
[Write one sentence interpreting Task 3 results.]

### Execution Logs
```text
[Paste full terminal output for Task 3 here]
```

---

## Task 4: Year Trend Analysis

Analyze how the total number of crimes changed over the years by extracting the year from the `Date` column (index 2) and counting crimes per year. This is exactly what Task 4 asks for in the milestone. :contentReference[oaicite:2]{index=2}

**Mapper:** `mapper_task4.py`  
**Reducer:** `reducer_sum.py`

### Command
```bash
mapred streaming \
-files mapper_task4.py,reducer_sum.py \
-mapper 'python3 mapper_task4.py' \
-reducer 'python3 reducer_sum.py' \
-input /data/chicago_crimes.csv \
-output /user/fsad/project/m1/task4
```

### Top 5 years by crime count
```text
2001    467301
2002    205267
2023    81461
2025    12710
2022    4678
```

### Interpretation
Crime counts are highest in 2001 and 2002, while later years are much lower, suggesting the dataset coverage or reporting volume varies significantly across years.

### Execution Logs
```text
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows

PS C:\WINDOWS\System32> ssh fsad@134.209.172.50
fsad@134.209.172.50's password:
Welcome to Ubuntu 22.04.5 LTS (GNU/Linux 5.15.0-170-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Thu Mar 26 20:14:15 UTC 2026

  System load:  0.32               Processes:             127
  Usage of /:   21.7% of 77.35GB   Users logged in:       2
  Memory usage: 50%                IPv4 address for eth0: 134.209.172.50
  Swap usage:   0%                 IPv4 address for eth0: 10.17.0.5

Expanded Security Maintenance for Applications is not enabled.

15 updates can be applied immediately.
3 of these updates are standard security updates.
To see these additional updates run: apt list --upgradable

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status

New release '24.04.4 LTS' available.
Run 'do-release-upgrade' to upgrade to it.

*** System restart required ***
Last login: Thu Mar 26 19:25:01 2026 from 50.60.101.184
fsad@master-node:~$ source /etc/profile.d/hadoop.sh
hdfs dfs -rm -r /user/fsad/project/m1/task4
mapred streaming \
-files mapper_task4.py,reducer_sum.py \
-mapper 'python3 mapper_task4.py' \
-reducer 'python3 reducer_sum.py' \
-input /data/chicago_crimes.csv \
-output /user/fsad/project/m1/task4
Deleted /user/fsad/project/m1/task4
packageJobJar: [] [/opt/hadoop-3.4.1/share/hadoop/tools/lib/hadoop-streaming-3.4.1.jar] /tmp/streamjob7336719525864906013.jar tmpDir=null
2026-03-26 20:14:42,033 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-03-26 20:14:42,376 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-03-26 20:14:42,864 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/fsad/.staging/job_1771402826595_0252
2026-03-26 20:14:45,068 INFO mapred.FileInputFormat: Total input files to process : 1
2026-03-26 20:14:45,093 INFO net.NetworkTopology: Adding a new node: /default-rack/164.92.103.148:9866
2026-03-26 20:14:45,094 INFO net.NetworkTopology: Adding a new node: /default-rack/146.190.147.119:9866
2026-03-26 20:14:45,697 INFO mapreduce.JobSubmitter: number of splits:2
2026-03-26 20:14:46,490 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1771402826595_0252
2026-03-26 20:14:46,490 INFO mapreduce.JobSubmitter: Executing with tokens: []
2026-03-26 20:14:46,781 INFO conf.Configuration: resource-types.xml not found
2026-03-26 20:14:46,781 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
2026-03-26 20:14:46,879 INFO impl.YarnClientImpl: Submitted application application_1771402826595_0252
2026-03-26 20:14:46,928 INFO mapreduce.Job: The url to track the job: http://master-node:8088/proxy/application_1771402826595_0252/
2026-03-26 20:14:46,929 INFO mapreduce.Job: Running job: job_1771402826595_0252
2026-03-26 20:15:05,688 INFO mapreduce.Job: Job job_1771402826595_0252 running in uber mode : false
2026-03-26 20:15:05,690 INFO mapreduce.Job:  map 0% reduce 0%
2026-03-26 20:15:32,120 INFO mapreduce.Job:  map 100% reduce 0%
2026-03-26 20:15:44,561 INFO mapreduce.Job:  map 100% reduce 100%
2026-03-26 20:15:47,507 INFO mapreduce.Job: Job job_1771402826595_0252 completed successfully
2026-03-26 20:15:47,791 INFO mapreduce.Job: Counters: 54
        File System Counters
                FILE: Number of bytes read=7137663
                FILE: Number of bytes written=15218300
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=181964998
                HDFS: Number of bytes written=245
                HDFS: Number of read operations=11
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=2
                HDFS: Number of bytes read erasure-coded=0
        Job Counters
                Launched map tasks=2
                Launched reduce tasks=1
                Data-local map tasks=2
                Total time spent by all maps in occupied slots (ms)=98640
                Total time spent by all reduces in occupied slots (ms)=19878
                Total time spent by all map tasks (ms)=49320
                Total time spent by all reduce tasks (ms)=9939
                Total vcore-milliseconds taken by all map tasks=49320
                Total vcore-milliseconds taken by all reduce tasks=9939
                Total megabyte-milliseconds taken by all map tasks=25251840
                Total megabyte-milliseconds taken by all reduce tasks=5088768
        Map-Reduce Framework
                Map input records=793074
                Map output records=793073
                Map output bytes=5551511
                Map output materialized bytes=7137669
                Input split bytes=198
                Combine input records=0
                Combine output records=0
                Reduce input groups=25
                Reduce shuffle bytes=7137669
                Reduce input records=793073
                Reduce output records=25
                Spilled Records=1586146
                Shuffled Maps =2
                Failed Shuffles=0
                Merged Map outputs=2
                GC time elapsed (ms)=779
                CPU time spent (ms)=8050
                Physical memory (bytes) snapshot=651743232
                Virtual memory (bytes) snapshot=6563844096
                Total committed heap usage (bytes)=347959296
                Peak Map Physical memory (bytes)=253624320
                Peak Map Virtual memory (bytes)=2185199616
                Peak Reduce Physical memory (bytes)=149004288
                Peak Reduce Virtual memory (bytes)=2193735680
        Shuffle Errors
                BAD_ID=0
                CONNECTION=0
                IO_ERROR=0
                WRONG_LENGTH=0
                WRONG_MAP=0
                WRONG_REDUCE=0
        File Input Format Counters
                Bytes Read=181964800
        File Output Format Counters
                Bytes Written=245
2026-03-26 20:15:47,792 INFO streaming.StreamJob: Output directory: /user/fsad/project/m1/task4
```

## Task 5: Arrest Rate Analysis

### Research Question
What percentage of crimes result in an arrest?

### Command
```bash
mapred streaming \
-files mapper_task5.py,reducer_sum.py \
-mapper 'python3 mapper_task5.py' \
-reducer 'python3 reducer_sum.py' \
-input /data/chicago_crimes.csv \
-output /user/[your_id]/project/m1/task5
```

### Results
```text
[Paste task 5 output here, ex:
false XXXXX
true  XXXXX]
```

### Calculated Arrest Rate
```text
[Paste calculated arrest rate here]
```

### Interpretation
[Write one sentence interpreting Task 5 results.]

### Execution Logs
```text
[Paste full terminal output for Task 5 here]
```

---

## Member Contributions

| Member | Contribution |
|---|---|
| Fjr Sad | Wrote `mapper_task4.py`, opened PR, merged Task 4, tested locally, executed Task 4 on the cluster, and added Task 4 results. |
| [Member 2 Name] | Wrote `mapper_task2.py`, tested and executed Task 2, added Task 2 results. |
| [Member 3 Name] | Wrote `mapper_task3.py`, tested and executed Task 3, added Task 3 results. |
| [Member 4 Name] | Wrote `mapper_task5.py`, tested and executed Task 5, added Task 5 results. |
| [Leader Name] | Created repository, added collaborators, set folder structure, committed shared `reducer_sum.py`. |
