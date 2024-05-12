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
37            print("Generate job list over")
38            return
39        else:
40            index = index
41            print("Job pid is {}".format(index))
42            ArrivalTime = int(input("Input ArrivalTime: "))
43            Time = int(input("Input Time: "))
44            
45            p = Job(index, ArrivalTime, Time)
46            SJF.jobs.append(p)
47
48            self.InputWithRecursion(n-1, index+1)
49
50
51if __name__ == '__main__':
52
53    S = SJF()
54
55    if args.run == 1:
56        jobs = [
57            Job(“A”,3,2 ),
58            Job(“B”,1,0 ),
59            Job(“C”,2,1 ),    
62        ]
63        AvgWaitingTime = S.SJF_Scheduling(jobs)
64        print("AvgWaitingTime is {}".format(AvgWaitingTime))
65
66    elif args.run == 2:
67        ProNum = input("Input Job num: ")
68        S.InputFromOutside(int(ProNum))
69
70    else:
71        ProNum = input("Input Job num: ")
72        S.InputWithRecursion(int(ProNum), 1)
