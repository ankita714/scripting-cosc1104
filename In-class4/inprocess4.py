
# Author:Ankita (100941771), Anita Mohan (100884879)
# Date: November 2, 2024
""" In this program we filters AWS EC2 instances by user defined CPU and memory requirements. 
we get user input their minimum and optional maximum values, and the app loads instance details from a JSON file. 
then we identify and displays instances that meet the criteria, simplifying the search for suitable EC2 types."""

import json

# Function to load EC2 instance data from a JSON file
def to_extract_number(text):
    parts = text.split()
    if parts and parts[0].replace('.', '', 1).isdigit():
        return float(parts[0])
    return None

# Function to get user input for CPU and memory requirements
def getting_user_input(prompt, allow_optional=False):
    value = input(prompt).strip()
    return float(value) if value else None if allow_optional else 0

def load_ec2_instances( filename ="ec2_instance_types.json"):
    with open(filename, "r") as file:
        return json.load(file)

def filter_instances(instances, min_cpu, max_cpu, min_memory, max_memory):

    filtered = []
    for instance in instances:
        cpu = to_extract_number(instance.get("vcpu", ""))
        memory = to_extract_number(instance.get("memory", ""))
        if cpu is not None and memory is not None:
            if (min_cpu <= cpu <= (max_cpu if max_cpu else float('inf'))) and \
               (min_memory <= memory <= (max_memory if max_memory else float('inf'))):
                filtered.append(instance)
    return filtered

def display_instances(instances):
    if not instances:
        print("\nNo matching EC2 Instances found.")
        return
    
    print("\n*** Matching EC2 Instances: ***")
    for instance in instances:
        print(f"- {instance['name']}: \n CPU: {instance['vcpu']}, \n Memory: {instance['memory']}, \n Storage: {instance['storage']}\n\n ")

def main():
    print("EC2 Instance Finder")

    min_cpu = getting_user_input("Enter minimum CPU cores required: ")
    max_cpu = getting_user_input("Enter maximum CPU cores allowed (optional): ", allow_optional=True)
    min_memory = getting_user_input("Enter minimum memory (GiB) required: ")
    max_memory = getting_user_input("Enter maximum memory (GiB) allowed (optional): ", allow_optional=True)

    instances = load_ec2_instances()
    matching_instances = filter_instances(instances, min_cpu, max_cpu, min_memory, max_memory)
    display_instances(matching_instances)

if __name__ == "__main__":
    main()
