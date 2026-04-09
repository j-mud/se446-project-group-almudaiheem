# SE446-Project-Group-Almudaiheem
Repository for SE446 (Intro to Big Data) Term project.

# SE446 Project Milestone 1: Chicago Crime Analytics with MapReduce

## Group Name
SE446-Project-Group-Almudaiheem

## Team Members

| Name | Student ID | Role / Task |
|---|---:|---|
| Aljohara Almudaiheem| 231383 | Task 1 — Repo Setup, Shared Reducer, README |
| Laura Alsubaie | 231747 | Task 2 — Crime Type Distribution |
| Joud Alhozami | 231682 | Task 3 — Location Hotspots |
| Fjr Sad | 231722 | Task 4 — Year Trend Analysis |
| Layan Al Shammari | 231822 | Task 5 — Arrest Rate |

### NOTE
There is an error when adding team members to the team on the AssessX website. You can find the team’s information in the table above and in the collaborators section of this repository.

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
[paste top 5 lines from task 2 output hereeeee]
```

### Interpretation
[write one sentence about task 2 results]

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
RESIDENCE	7
STREET	6
COMMERCIAL	3
APARTMENT	3
SIDEWALK	2
```

### Interpretation
The results shows us that the most common crimes occur in residence locations followed by street and commercial areas, indicating that crime is concentrated in residential and public environments.

### Execution Logs
```text
joud@Jouds-MBP-2 se446-project-group-almudaiheem % cat chicago_crimes.csv | python3 src/mapper_task3.py | sort | python3 src/reducer_sum.py
APARTMENT	3
BAR OR TAVERN	1
COMMERCIAL	3
CTA BUS	1
CTA PLATFORM	1
HOTEL	1
PARKING LOT	3
RESIDENCE	7
RESTAURANT	1
RETAIL STORE	1
SIDEWALK	2
STREET	6

```

---

## Task 4: Year Trend Analysis

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
Crime counts are highest in 2001 and 2002, but later years are much lower, showing that the dataset coverage or reporting varies significantly across years.

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
-mapper "python3 mapper_task5.py" \
-reducer "python3 reducer_sum.py" \
-input /data/chicago_crimes.csv \
-output /user/lmalshammari/project/m1/task5
```

### Results
```text
false   571140
true    221932
```

### Calculated Arrest Rate
```text
221932/(221932+571140)*100= 27.9838 , Aproximetly 28%
```

### Interpretation
About 28% of crimes resulted in an arrest, which means most crimes didnt lead to an arrest.

### Execution Logs
```text
Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

Install the latest PowerShell for new features and improvements! https://aka.ms/PSWindows

PS C:\Users\96650> cd Downloads
PS C:\Users\96650\Downloads> scp mapper_task5.py reducer_sum.py lmalshammari@134.209.172.50:~/
lmalshammari@134.209.172.50's password:
mapper_task5.py               100%  236     1.2KB/s   00:00
reducer_sum.py                100%  521     2.2KB/s   00:00
PS C:\Users\96650\Downloads> ssh lmalshammari@134.209.172.50
lmalshammari@134.209.172.50's password:
Welcome to Ubuntu 22.04.5 LTS (GNU/Linux 5.15.0-170-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Thu Mar 26 19:21:33 UTC 2026

  System load:  0.09               Processes:             129
  Usage of /:   21.7% of 77.35GB   Users logged in:       2
  Memory usage: 51%                IPv4 address for eth0: 134.209.172.50
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
Last login: Thu Feb  5 07:29:52 2026 from 188.48.100.201
lmalshammari@master-node:~$ source /etc/profile.d/hadoop.sh
lmalshammari@master-node:~$ ls
bigfile.dat  mapper_task5.py  reducer_sum.py
lmalshammari@master-node:~$ hdfs dfs -rm -r /user/lmalshammari/project/m1/task5
rm: `/user/lmalshammari/project/m1/task5': No such file or directory
lmalshammari@master-node:~$ mapred streaming \
-files mapper_task5.py,reducer_sum.py \
-mapper "python3 mapper_task5.py" \
-reducer "python3 reducer_sum.py" \
-input /data/chicago_crimes.csv \
-output /user/lmalshammari/project/m1/task5
packageJobJar: [] [/opt/hadoop-3.4.1/share/hadoop/tools/lib/hadoop-streaming-3.4.1.jar] /tmp/streamjob17891697242423119770.jar tmpDir=null
2026-03-26 19:27:45,511 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-03-26 19:27:45,865 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-03-26 19:27:46,372 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/lmalshammari/.staging/job_1771402826595_0249
2026-03-26 19:27:48,181 INFO mapred.FileInputFormat: Total input files to process : 1
2026-03-26 19:27:48,213 INFO net.NetworkTopology: Adding a new node: /default-rack/146.190.147.119:9866
2026-03-26 19:27:48,214 INFO net.NetworkTopology: Adding a new node: /default-rack/164.92.103.148:9866
2026-03-26 19:27:48,839 INFO mapreduce.JobSubmitter: number of splits:2
2026-03-26 19:27:49,990 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1771402826595_0249
2026-03-26 19:27:49,990 INFO mapreduce.JobSubmitter: Executing with tokens: []
2026-03-26 19:27:50,319 INFO conf.Configuration: resource-types.xml not found
2026-03-26 19:27:50,320 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
2026-03-26 19:27:50,444 INFO impl.YarnClientImpl: Submitted application application_1771402826595_0249
2026-03-26 19:27:50,504 INFO mapreduce.Job: The url to track the job: http://master-node:8088/proxy/application_1771402826595_0249/
2026-03-26 19:27:50,507 INFO mapreduce.Job: Running job: job_1771402826595_0249
2026-03-26 19:28:08,381 INFO mapreduce.Job: Job job_1771402826595_0249 running in uber mode : false
2026-03-26 19:28:08,383 INFO mapreduce.Job:  map 0% reduce 0%
2026-03-26 19:28:33,707 INFO mapreduce.Job:  map 100% reduce 0%
2026-03-26 19:28:44,476 INFO mapreduce.Job: Task Id : attempt_1771402826595_0249_r_000000_0, Status : FAILED
Error: java.lang.RuntimeException: PipeMapRed.waitOutputThreads(): subprocess failed with code 1
        at org.apache.hadoop.streaming.PipeMapRed.waitOutputThreads(PipeMapRed.java:326)
        at org.apache.hadoop.streaming.PipeMapRed.mapRedFinished(PipeMapRed.java:539)
        at org.apache.hadoop.streaming.PipeReducer.reduce(PipeReducer.java:127)
        at org.apache.hadoop.mapred.ReduceTask.runOldReducer(ReduceTask.java:445)
        at org.apache.hadoop.mapred.ReduceTask.run(ReduceTask.java:393)
        at org.apache.hadoop.mapred.YarnChild$2.run(YarnChild.java:178)
        at java.base/java.security.AccessController.doPrivileged(Native Method)
        at java.base/javax.security.auth.Subject.doAs(Subject.java:423)
        at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1953)
        at org.apache.hadoop.mapred.YarnChild.main(YarnChild.java:172)

2026-03-26 19:28:55,285 INFO mapreduce.Job: Task Id : attempt_1771402826595_0249_r_000000_1, Status : FAILED
Error: java.lang.RuntimeException: PipeMapRed.waitOutputThreads(): subprocess failed with code 1
        at org.apache.hadoop.streaming.PipeMapRed.waitOutputThreads(PipeMapRed.java:326)
        at org.apache.hadoop.streaming.PipeMapRed.mapRedFinished(PipeMapRed.java:539)
        at org.apache.hadoop.streaming.PipeReducer.reduce(PipeReducer.java:127)
        at org.apache.hadoop.mapred.ReduceTask.runOldReducer(ReduceTask.java:445)
        at org.apache.hadoop.mapred.ReduceTask.run(ReduceTask.java:393)
        at org.apache.hadoop.mapred.YarnChild$2.run(YarnChild.java:178)
        at java.base/java.security.AccessController.doPrivileged(Native Method)
        at java.base/javax.security.auth.Subject.doAs(Subject.java:423)
        at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1953)
        at org.apache.hadoop.mapred.YarnChild.main(YarnChild.java:172)

2026-03-26 19:29:06,108 INFO mapreduce.Job: Task Id : attempt_1771402826595_0249_r_000000_2, Status : FAILED
Error: java.lang.RuntimeException: PipeMapRed.waitOutputThreads(): subprocess failed with code 1
        at org.apache.hadoop.streaming.PipeMapRed.waitOutputThreads(PipeMapRed.java:326)
        at org.apache.hadoop.streaming.PipeMapRed.mapRedFinished(PipeMapRed.java:539)
        at org.apache.hadoop.streaming.PipeReducer.reduce(PipeReducer.java:127)
        at org.apache.hadoop.mapred.ReduceTask.runOldReducer(ReduceTask.java:445)
        at org.apache.hadoop.mapred.ReduceTask.run(ReduceTask.java:393)
        at org.apache.hadoop.mapred.YarnChild$2.run(YarnChild.java:178)
        at java.base/java.security.AccessController.doPrivileged(Native Method)
        at java.base/javax.security.auth.Subject.doAs(Subject.java:423)
        at org.apache.hadoop.security.UserGroupInformation.doAs(UserGroupInformation.java:1953)
        at org.apache.hadoop.mapred.YarnChild.main(YarnChild.java:172)

2026-03-26 19:29:19,179 INFO mapreduce.Job:  map 100% reduce 100%
2026-03-26 19:29:21,943 INFO mapreduce.Job: Job job_1771402826595_0249 failed with state FAILED due to: Task failed task_1771402826595_0249_r_000000
Job failed as tasks failed. failedMaps:0 failedReduces:1 killedMaps:0 killedReduces: 0

2026-03-26 19:29:22,270 INFO mapreduce.Job: Counters: 40
        File System Counters
                FILE: Number of bytes read=0
                FILE: Number of bytes written=8396918
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=181964998
                HDFS: Number of bytes written=0
                HDFS: Number of read operations=6
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=0
                HDFS: Number of bytes read erasure-coded=0
        Job Counters
                Failed reduce tasks=4
                Launched map tasks=2
                Launched reduce tasks=4
                Data-local map tasks=2
                Total time spent by all maps in occupied slots (ms)=90744
                Total time spent by all reduces in occupied slots (ms)=67648
                Total time spent by all map tasks (ms)=45372
                Total time spent by all reduce tasks (ms)=33824
                Total vcore-milliseconds taken by all map tasks=45372
                Total vcore-milliseconds taken by all reduce tasks=33824
                Total megabyte-milliseconds taken by all map tasks=23230464
                Total megabyte-milliseconds taken by all reduce tasks=17317888
        Map-Reduce Framework
                Map input records=793074
                Map output records=793072
                Map output bytes=6181870
                Map output materialized bytes=7768026
                Input split bytes=198
                Combine input records=0
                Spilled Records=793072
                Failed Shuffles=0
                Merged Map outputs=0
                GC time elapsed (ms)=593
                CPU time spent (ms)=5780
                Physical memory (bytes) snapshot=506105856
                Virtual memory (bytes) snapshot=4368859136
                Total committed heap usage (bytes)=303190016
                Peak Map Physical memory (bytes)=253890560
                Peak Map Virtual memory (bytes)=2184949760
        File Input Format Counters
                Bytes Read=181964800
2026-03-26 19:29:22,271 ERROR streaming.StreamJob: Job not successful!
Streaming Command Failed!
lmalshammari@master-node:~$ sed -n '1,200p' reducer_sum.py
import sys

current_key = None
current_count = 0

for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t', 1)

    try:
        count = int(value)
    except ValueError:
        continue

    if key == current_key:
        current_count += count
    else:
        if current_key is not None:
            print(f'{current_key}\t{current_count}')
        current_key = key
        current_count = count

if current_key is not None:
    print(f'{current_key}\t{current_count}')lmalshammari@master-node:~$ hdflmalshammari@master-node:~$ hdfs dfs -cat /data/chicago_crimes_sample.csv | head -200 | python3 mapper_task5.py | sort | python3 reducer_sum.py
cat: Unable to write to output stream.
FEET    5
false   130
true    64
lmalshammari@master-node:~$ cd Downloads
-bash: cd: Downloads: No such file or directory


lmalshammari@master-node:~$ hdfs dfs -cat /data/chicago_crimes_sample.csv | head -200 | python3 mapper_task5.py | sort | python3 reducer_sum.py
  File "/home/lmalshammari/mapper_task5.py", line 16
    print(f'{arrested}\t1')import sys
                           ^^^^^^
SyntaxError: invalid syntax
cat: Unable to write to output stream.
lmalshammari@master-node:~$ nano mapper_task5.py
lmalshammari@master-node:~$ nano mapper_task5.py
lmalshammari@master-node:~$ hdfs dfs -cat /data/chicago_crimes_sample.csv | head -200 | python3 mapper_task5.py | sort | python3 reducer_sum.py
false   131
true    68
cat: Unable to write to output stream.
lmalshammari@master-node:~$ hdfs dfs -rm -r /user/lmalshammari/project/m1/task5
Deleted /user/lmalshammari/project/m1/task5
lmalshammari@master-node:~$ mapred streaming \
-files mapper_task5.py,reducer_sum.py \
-mapper "python3 mapper_task5.py" \
-reducer "python3 reducer_sum.py" \
-input /data/chicago_crimes.csv \
-output /user/lmalshammari/project/m1/task5
packageJobJar: [] [/opt/hadoop-3.4.1/share/hadoop/tools/lib/hadoop-streaming-3.4.1.jar] /tmp/streamjob4190262929811248097.jar tmpDir=null
2026-03-26 20:08:05,357 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-03-26 20:08:05,684 INFO client.DefaultNoHARMFailoverProxyProvider: Connecting to ResourceManager at master-node/134.209.172.50:8032
2026-03-26 20:08:06,077 INFO mapreduce.JobResourceUploader: Disabling Erasure Coding for path: /tmp/hadoop-yarn/staging/lmalshammari/.staging/job_1771402826595_0251
2026-03-26 20:08:07,755 INFO mapred.FileInputFormat: Total input files to process : 1
2026-03-26 20:08:07,780 INFO net.NetworkTopology: Adding a new node: /default-rack/146.190.147.119:9866
2026-03-26 20:08:07,781 INFO net.NetworkTopology: Adding a new node: /default-rack/164.92.103.148:9866
2026-03-26 20:08:08,332 INFO mapreduce.JobSubmitter: number of splits:2
2026-03-26 20:08:09,175 INFO mapreduce.JobSubmitter: Submitting tokens for job: job_1771402826595_0251
2026-03-26 20:08:09,176 INFO mapreduce.JobSubmitter: Executing with tokens: []
2026-03-26 20:08:09,492 INFO conf.Configuration: resource-types.xml not found
2026-03-26 20:08:09,493 INFO resource.ResourceUtils: Unable to find 'resource-types.xml'.
2026-03-26 20:08:09,621 INFO impl.YarnClientImpl: Submitted application application_1771402826595_0251
2026-03-26 20:08:09,684 INFO mapreduce.Job: The url to track the job: http://master-node:8088/proxy/application_1771402826595_0251/
2026-03-26 20:08:09,686 INFO mapreduce.Job: Running job: job_1771402826595_0251
2026-03-26 20:08:27,517 INFO mapreduce.Job: Job job_1771402826595_0251 running in uber mode : false
2026-03-26 20:08:27,519 INFO mapreduce.Job:  map 0% reduce 0%
2026-03-26 20:08:56,671 INFO mapreduce.Job:  map 100% reduce 0%
2026-03-26 20:09:11,106 INFO mapreduce.Job:  map 100% reduce 100%
2026-03-26 20:09:13,873 INFO mapreduce.Job: Job job_1771402826595_0251 completed successfully
2026-03-26 20:09:14,132 INFO mapreduce.Job: Counters: 54
        File System Counters
                FILE: Number of bytes read=7708794
                FILE: Number of bytes written=16360874
                FILE: Number of read operations=0
                FILE: Number of large read operations=0
                FILE: Number of write operations=0
                HDFS: Number of bytes read=181964998
                HDFS: Number of bytes written=25
                HDFS: Number of read operations=11
                HDFS: Number of large read operations=0
                HDFS: Number of write operations=2
                HDFS: Number of bytes read erasure-coded=0
        Job Counters
                Launched map tasks=2
                Launched reduce tasks=1
                Data-local map tasks=2
                Total time spent by all maps in occupied slots (ms)=101436
                Total time spent by all reduces in occupied slots (ms)=23644
                Total time spent by all map tasks (ms)=50718
                Total time spent by all reduce tasks (ms)=11822
                Total vcore-milliseconds taken by all map tasks=50718
                Total vcore-milliseconds taken by all reduce tasks=11822
                Total megabyte-milliseconds taken by all map tasks=25967616
                Total megabyte-milliseconds taken by all reduce tasks=6052864
        Map-Reduce Framework
                Map input records=793074
                Map output records=793072
                Map output bytes=6122644
                Map output materialized bytes=7708800
                Input split bytes=198
                Combine input records=0
                Combine output records=0
                Reduce input groups=2
                Reduce shuffle bytes=7708800
                Reduce input records=793072
                Reduce output records=2
                Spilled Records=1586144
                Shuffled Maps =2
                Failed Shuffles=0
                Merged Map outputs=2
                GC time elapsed (ms)=819
                CPU time spent (ms)=8430
                Physical memory (bytes) snapshot=654041088
                Virtual memory (bytes) snapshot=6560694272
                Total committed heap usage (bytes)=348139520
                Peak Map Physical memory (bytes)=252932096
                Peak Map Virtual memory (bytes)=2186350592
                Peak Reduce Physical memory (bytes)=150249472
                Peak Reduce Virtual memory (bytes)=2190893056
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
                Bytes Written=25
2026-03-26 20:09:14,138 INFO streaming.StreamJob: Output directory: /user/lmalshammari/project/m1/task5
lmalshammari@master-node:~$ hdfs dfs -cat /user/lmalshammari/project/m1/task5/part-00000
false   571140
true    221932
lmalshammari@master-node:~$ hdfs dfs -cat /user/lmalshammari/project/m1/task5/part-00000 | sort -k2 -rn | head -5
false   571140
true    221932
lmalshammari@master-node:~$ exit
logout
Connection to 134.209.172.50 closed.
PS C:\Users\96650\Downloads> cd Downloads
cd : Cannot find path 'C:\Users\96650\Downloads\Downloads' because it does not exist.
At line:1 char:1
+ cd Downloads
+ ~~~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (C:\Users\96650\Downloads\Downloads:String) [Set-Location], ItemNotFoundException
    + FullyQualifiedErrorId : PathNotFound,Microsoft.PowerShell.Commands.SetLocationCommand

PS C:\Users\96650\Downloads> git clone https://github.com/j-mud/se446-project-group-almudaiheem.git
Cloning into 'se446-project-group-almudaiheem'...
remote: Enumerating objects: 96, done.
remote: Counting objects: 100% (96/96), done.
remote: Compressing objects: 100% (88/88), done.
remote: Total 96 (delta 34), reused 11 (delta 3), pack-reused 0 (from 0)
Receiving objects: 100% (96/96), 32.23 KiB | 523.00 KiB/s, done.
Resolving deltas: 100% (34/34), done.
PS C:\Users\96650\Downloads> cd se446-project-group-almudaiheem
PS C:\Users\96650\Downloads\se446-project-group-almudaiheem> git checkout -b task5-Layan
Switched to a new branch 'task5-Layan'
PS C:\Users\96650\Downloads\se446-project-group-almudaiheem> git status
On branch task5-Layan
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        src/mapper_task5.py

nothing added to commit but untracked files present (use "git add" to track)
PS C:\Users\96650\Downloads\se446-project-group-almudaiheem> git add src/mapper_task5.py
PS C:\Users\96650\Downloads\se446-project-group-almudaiheem> git commit -m "Task 5: Add mapper_task5.py"
Author identity unknown

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got '96650@Byte_Me.(none)')
PS C:\Users\96650\Downloads\se446-project-group-almudaiheem> git config --global user.name "Layan Alshammari"
PS C:\Users\96650\Downloads\se446-project-group-almudaiheem> git config --global user.email "alshammarilayan@gmail.com"
PS C:\Users\96650\Downloads\se446-project-group-almudaiheem> git commit -m "Task 5: Add mapper_task5.py"
[task5-Layan bb6cc83] Task 5: Add mapper_task5.py
 1 file changed, 12 insertions(+)
 create mode 100644 src/mapper_task5.py
PS C:\Users\96650\Downloads\se446-project-group-almudaiheem> git push origin task5-Layan
Enumerating objects: 62, done.
Counting objects: 100% (60/60), done.
Delta compression using up to 16 threads
Compressing objects: 100% (39/39), done.
Writing objects: 100% (53/53), 20.48 KiB | 10.24 MiB/s, done.
Total 53 (delta 17), reused 47 (delta 14), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (17/17), completed with 1 local object.
remote:
remote: Create a pull request for 'task5-Layan' on GitHub by visiting:
remote:      https://github.com/j-mud/se446-project-group-almudaiheem/pull/new/task5-Layan
remote:
To https://github.com/j-mud/se446-project-group-almudaiheem.git
 * [new branch]      task5-Layan -> task5-Layan
```

---

## Member Contributions

| Member | Contribution |
|---|---|
| Aljohara Almudaiheem| Created the repository structure, added the shared reducer_sum.py, and handled Task 1 setup requirements. |
| Laura | Implemented mapper_task2.py for crime type distribution and contributed Task 2 results. |
| Joud | Implemented mapper_task3.py for location hotspot analysis and contributed Task 3 results. |
| Fjr Sad | Implemented mapper_task4.py for year trend analysis, tested it locally, ran it on the Hadoop cluster, collected the output and top 5 results, and documented Task 4 in the README. |
| Layan Alshammari| Implemented mapper_task5.py for arrest rate analysis and contributed Task 5 results. |
