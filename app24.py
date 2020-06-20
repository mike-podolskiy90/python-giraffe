# Reading files

# r read
# w write
# a append
# r+ read-write
employee_file = open("employees.txt", "r")

print(employee_file.readable())

print(employee_file.readline())

for employee in employee_file.readlines():
    print(employee)

employee_file.close()
