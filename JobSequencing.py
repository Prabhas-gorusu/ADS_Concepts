class Job:
    def __init__(self, job_id, deadline, profit):
        self.id = job_id
        self.deadline = deadline
        self.profit = profit

# Comparator function to sort jobs by descending profit
def job_sequencing(jobs):
    # Sort jobs by profit in descending order
    jobs.sort(key=lambda job: job.profit, reverse=True)

    n = len(jobs)
    slot = [-1] * n  # Time slots
    job_count = 0
    total_profit = 0

    for i in range(n):
        # Find a free slot from the job's deadline going backward
        for j in range(min(n, jobs[i].deadline) - 1, -1, -1):
            if slot[j] == -1:
                slot[j] = i  # Assign job index
                job_count += 1
                total_profit += jobs[i].profit
                break

    # Print results
    print("Job Sequence for maximum profit:")
    for i in range(n):
        if slot[i] != -1:
            job = jobs[slot[i]]
            print(f"Job ID: {job.id}, Deadline: {job.deadline}, Profit: {job.profit}")
    print(f"Total Jobs Scheduled: {job_count}")
    print(f"Total Profit: {total_profit}")

# Main execution
def main():
    n = int(input("Enter the number of jobs: "))
    jobs = []
    print("Enter job details (ID Deadline Profit):")
    for i in range(n):
        job_input = input(f"Job {i+1}: ").split()
        job_id, deadline, profit = map(int, job_input)
        jobs.append(Job(job_id, deadline, profit))

    job_sequencing(jobs)

if __name__ == "__main__":
    main()
