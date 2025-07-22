# # Get user input for basic salary
# basic_salary = float(input("Enter the basic salary: "))


# ta = basic_salary * 0.04  
# da = basic_salary * 0.30  
# hra = basic_salary * 0.15 


# tax = basic_salary * 0.03  
# pf = basic_salary * 0.12   


# gross_salary = basic_salary + ta + da + hra
# net_salary = gross_salary - (tax + pf)


# print(f"\nBasic Salary: {basic_salary:.2f}")
# print(f"Total Allowances: {ta + da + hra:.2f}")
# print(f"Total Deductions: {tax + pf:.2f}")
# print(f"Net Salary: {net_salary:.2f}")




marks = []  
total_subjects = 5  

for i in range(1, total_subjects + 1):
    mark = float(input(f"Enter marks for subject {i}: "))  
    marks.append(mark) 

# Calculate total and percentage
total_marks = sum(marks) 
percentage = (total_marks / (total_subjects * 100)) * 100  


print("\n--- Results ---")
print(f"Total Marks: {total_marks}")
print(f"Percentage: {percentage:.2f}%")
