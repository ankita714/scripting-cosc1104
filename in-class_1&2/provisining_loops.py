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
remaining_cpu_core = TOTAL_AVAILABLE_CPU
remaining_memory_gb = TOTAL_AVAILABLE_MEMORY

# lists to store allocated and pending requests
allocated_resources = []
pending_requests = []

# Loop to handle multiple resource requests
is_continuing = "yes"

while is_continuing.lower() == "yes":
    # Requesting the user to enter the required details username, required CPU core, and memory
    username = input("Enter username: ")
    requested_cpu = int(input("Enter the number of CPU cores required: "))
    requested_memory = float(input("Enter the amount of memory (in GB) required: "))

    # Check if the requested resources are valid and available
    if requested_cpu < 0 or requested_memory < 0:
        print("Invalid input: CPU cores and memory must be non-negative numbers.")
    elif requested_cpu <= remaining_cpu_core and requested_memory <= remaining_memory_gb:
        # Allocate resources
        allocated_resources.append([username, requested_cpu, requested_memory])
        remaining_cpu_core -= requested_cpu
        remaining_memory_gb -= requested_memory
        print(f"Resources allocated to {username} successfully!")
    else:
        # Add to pending requests
        pending_requests.append([username, requested_cpu, requested_memory])
        print(f"Resources not available for {username}, added to pending requests.")

    # Check if the user wants to make another request
    is_continuing = input("Do you want to make another request? (yes/no): ")

# Display the results in a table-like format
print("\n***** Allocated Resources: *****")
print("-" * 40)
for detail in allocated_resources:
    
    print(f"Username: {detail[0]} \t CPU cores: {detail[1]} \t Memory (GB): {detail[2]}")
    

print("\n***** Pending Requests: *****")
print("-" * 40)
for record in pending_requests:
    
    print(f"Username: {record[0]} \t CPU cores: {record[1]} \t Memory (GB): {record[2]}")
   