class job:
    def __init__(self, name, Time,arriveTime):
        self.name = name
        self.Time = Time
        self.ArriveTime = ArriveTime
class SJF:
2    def SJF_Scheduling(self, jobs):
3        print("Initial number of jobs is {}".format(len(jobs)))
4        jobs.sort(key=lambda x: x.Time)  # 按照作业长度排序
5        CompletionTime = 0
6        WaitingTime = 0
7        CyclingTime = 0
8
9        for job in jobs:
10            CompletionTime = max(CompletionTime, job.ArrivalTime) + job.Time
11            CyclingTime = CompletionTime - job.ArrivalTime
12            WaitingTime += max(0, CompletionTime - job.ArrivalTime - job.Time)
13            print("name is {}, CompletionTime is {}, CyclingTime is {}".format(job.name, CompletionTime, CyclingTime))
14            
15        AvgWaitingTime = WaitingTime / len(jobs)
16
17        return AvgWaitingTime
18
19    def InputFromOutside(self, n):
20        jobs = []
21        for i in range(n):
22            print("Job pid is {}".format(i+1))
23            ArrivalTime = int(input("Input ArrivalTime: "))
24            Time = int(input("Input Time: "))
25            
26            p = Job(i+1, ArrivalTime, Time)
27            jobs.append(p)
28
29        SJF.SJF_Scheduling(jobs)
30        print("Generate job list over")
31
32    jobs = []  # List for Recursion
33
34    def InputWithRecursion(self, n, index):
35        if n == 0:
36            AvgWaitingTime = SJF.SJF_Scheduling(SJF.jobs)
