"""
provisioning_loops.py
Name = Ankita
Date = 28-9-2024
Description : This script uses lists and loops to track allocated and 
waiting resources as it simulates cloud resource provisioning with various user requests.

"""


# Constants 
TOTAL_AVAILABLE_CPU = 32  # The total number of CPU cores available
TOTAL_AVAILABLE_MEMORY = 128.0  # The total amount of memory available in gigabytes (GB)

# we need to consider the remaining capacity as total after every allocation.
remainingCpuCore = TOTAL_AVAILABLE_CPU
remainingMemoryGb = TOTAL_AVAILABLE_MEMORY

# lists to store allocated and pending requests
allocated_resources = []
pending_requests = []


is_continuing = "yes"

while is_continuing.lower() == "yes":
    # Requesting the user to enter the required details username, required CPU core, and memory
    username = input("Enter username: ")
    requested_cpu = int(input("Enter the number of CPU cores required: "))
    requested_memory = float(input("Enter the amount of memory (in GB) required: "))

    if requested_cpu < 0 or requested_memory < 0: # check for invalid enteries 
        print("Invalid input: CPU cores and memory must be non-negative numbers.")
    elif requested_cpu <= remainingCpuCore and requested_memory <= remainingMemoryGb: # check for CPU and memory availability
        # if available then allocate and add to allocated_resources list
        allocated_resources.append([username, requested_cpu, requested_memory])
        remainingCpuCore -= requested_cpu
        remainingMemoryGb -= requested_memory
        print(f"Resources allocated to {username} successfully!")
    else:
        # Else add to the pending_requests list
        pending_requests.append([username, requested_cpu, requested_memory])
        print(f"Resources not available for {username}, added to pending requests.")

    # Checking for continuation 
    is_continuing = input("Do you want to make more request? (yes/no): ")

# result table 
print("\n***** Allocated Resources: *****") # allocated resources table 
print("-" * 40)
for detail in allocated_resources:
    
    print(f"Username: {detail[0]} \t CPU cores: {detail[1]} \t Memory (GB): {detail[2]}")
    

print("\n***** Pending Requests: *****") # pending requests table 
print("-" * 40)
for detail in pending_requests:
    
    print(f"Username: {detail[0]} \t CPU cores: {detail[1]} \t Memory (GB): {detail[2]}")
   