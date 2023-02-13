def process_jobs(jobs):
    """
    This function takes in a list of jobs, where each job is represented as a tuple containing the start time, end time, and earnings.
    The function returns the number of remaining jobs and the total earnings.
    """
    n = len(jobs) # number of jobs
    total_earnings = 0 # initialize total earnings to 0
    remaining_jobs = n # initialize remaining jobs to the total number of jobs
    end_time = 0 # initialize the end time to 0

    # loop through each job
    for i in range(n):
        # if the start time of the current job is greater than or equal to the end time of the previous job
        if jobs[i][0] >= end_time:
            end_time = jobs[i][1] # update end time to the end time of the current job
            total_earnings += jobs[i][2] # add the earnings of the current job to the total earnings
            remaining_jobs -= 1 # decrement the remaining jobs by 1
    # return the remaining jobs and total earnings
    return remaining_jobs, total_earnings

def main():
    """
    The main function takes input for the number of jobs and the start time, end time, and earnings for each job.
    It then calls the process_jobs function and prints the number of remaining jobs and total earnings.
    """
    print("Enter the number of Jobs")
    num_jobs = int(input()) # input for the number of jobs
    jobs = [] # list to store jobs
    # loop through each job
    for i in range(num_jobs):
        print("Enter job start time, end time, and earnings")
        start_time = int(input().strip().replace(':', '')) # input for start time
        end_time = int(input().strip().replace(':', '')) # input for end time
        earnings = int(input()) # input for earnings
        jobs.append((start_time, end_time, earnings)) # append the job to the list

    remaining_jobs, total_earnings = process_jobs(jobs) # call the process_jobs function
    print("The number of tasks and earnings available for others")
    print("Task:", remaining_jobs)
    print("Earnings:", total_earnings)

if __name__ == '__main__':
    main()
