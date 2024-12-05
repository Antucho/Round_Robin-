# Round Robin Scheduling Algorithm

def round_robin(processes, burst_times, arrival_times, time_quantum):
    n = len(processes)
    remaining_burst_times = burst_times.copy()
    time = 0
    complete = 0
    waiting_times = [0] * n
    turnaround_times = [0] * n
    gantt_chart = []
    queue = []

    while complete < n:
        
        for i in range(n):
            if arrival_times[i] <= time and processes[i] not in queue and remaining_burst_times[i] > 0:
                queue.append(processes[i])

        if not queue:  
            time += 1
            continue

        
        current_process = queue.pop(0)
        index = processes.index(current_process)
        
        
        gantt_chart.append((current_process, time))
        execution_time = min(remaining_burst_times[index], time_quantum)
        time += execution_time
        remaining_burst_times[index] -= execution_time

        if remaining_burst_times[index] == 0:
            complete += 1
            turnaround_times[index] = time - arrival_times[index]
            waiting_times[index] = turnaround_times[index] - burst_times[index]
        else:
            
            queue.append(current_process)

    avg_turnaround_time = sum(turnaround_times) / n
    avg_waiting_time = sum(waiting_times) / n

    return avg_turnaround_time, avg_waiting_time, waiting_times, turnaround_times, gantt_chart, time


n = int(input("Enter the number of processes: "))
processes = []
burst_times = []
arrival_times = []

for i in range(n):
    process_name = input(f"Enter name for Process {i+1}: ")
    processes.append(process_name)
    burst_time = int(input(f"Enter burst time for Process {process_name}: "))
    burst_times.append(burst_time)
    arrival_time = int(input(f"Enter arrival time for Process {process_name}: "))
    arrival_times.append(arrival_time)

time_quantum = int(input("Enter the time quantum: "))


avg_tat, avg_wt, waiting_times, turnaround_times, gantt_chart, final_time = round_robin(processes, burst_times, arrival_times, time_quantum)


print("\nProcess\tBurst Time\tArrival Time\tWaiting Time\tTurnaround Time")
for i in range(len(processes)):
    print(f"{processes[i]}\t{burst_times[i]}\t\t{arrival_times[i]}\t\t{waiting_times[i]}\t\t{turnaround_times[i]}")

print(f"\nAverage Turnaround Time: {avg_tat:.2f} ms")
print(f"Average Waiting Time: {avg_wt:.2f} ms")


print("\nGantt Chart:")
for process, start_time in gantt_chart:
    print(f"| {process} ({start_time})", end=" ")
print(f"| End ({final_time})")
