"""
provisioning.py 
Name = Ankita
Date = 28-9-2024
Description: This script checks whether the requested resources are available based on a 
predefined limit for CPU cores and RAM, simulating cloud resource provisioning.

"""

# Constants
TOTAL_AVAILABLE_CPU = 32  # The total number of CPU cores available
TOTAL_AVAILABLE_MEMORY = 128.0  # The total amount of memory available in gigabytes (GB).

# User input
cpu_requested = int(input("Enter the number of CPU cores needed: "))
memory_requested = float(input("Enter the amount of memory (in GB) needed: "))

# Check if the requested resources can be provisioned
if cpu_requested > TOTAL_AVAILABLE_CPU or memory_requested > TOTAL_AVAILABLE_MEMORY: # statement for checking if the value do not exceed available value 
    print("Resource request exceeds capacity. Provisioning failed.")
elif cpu_requested < 0 or memory_requested < 0: # statement for controlling invalid inputs 
    print("Invalid input: CPU cores and memory must be non-negative numbers.")
else:
    print("Resources provisioned successfully!")
    remaining_cpu_core = TOTAL_AVAILABLE_CPU - cpu_requested # calculating remaining cpu 
    remaining_memory = TOTAL_AVAILABLE_MEMORY - memory_requested # calculating remaining memory 
    print(f"Remaining CPU Cores: {remaining_cpu_core}")
    print(f"Remaining Memory (GB): {remaining_memory}")
