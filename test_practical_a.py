"""
    Name = Ankita 
    Id = 100941771
    Date = Oct./15/2024
    Creating program for allocating users to three different departments.
    
"""
TOTAL_NUMBER_OF_DEPARTMENTS = 3
TOTAL_USERS = 32

    
department_first_users = int(input("Enter the number of users for first department: "))
department_second_users = int(input("Enter the number of users for second department:"))
    
first_two_departments_total = department_first_users+department_second_users
remaining_users = TOTAL_USERS-first_two_departments_total
if ( first_two_departments_total > TOTAL_USERS):
    print("You have exceeded the maximum allowable users")
elif(first_two_departments_total == TOTAL_USERS ):
    print("There are no additional users allowed")
else:
    print(f"Users still available", remaining_users)
 
    
print(f"Users in department first:",department_first_users)
print(f"Users indepartment Second:",department_second_users)
print(f"Remaining available users for department three: ",remaining_users)



   