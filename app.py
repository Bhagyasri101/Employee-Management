import database

USER_CHOICE = """
'a' to add a new employee
'l' to list all employees
's' to search for an employee details
'S' to search for an employee department
'd' to delete an employee
'p' to update an employee salary
'q' to quit

your choice: """

#Add an employee
def prompt_add_employee():
    emp_id = input("Enter Employee id:")
    name = input("Enter employee name:")
    department = input("Enter employee's department:")
    salary = float(input("Enter employee salary:"))
    experience = int(input("Enter employee's experience:"))

    database.insert_details(emp_id, name, department, salary, experience)

# List all employees
def list_employees():
    details = database.get_all_employee()

    for detail in details:
        print(
            f"{detail['name']} by {detail['emp_id']}"
            f" | department: {detail['department']}"
            f" | salary: {detail['salary']}"
            f" | experience: {detail['experience']}"
        )

# search employee by name
def prompt_search_details():
    name = input("Enter employee name:")
    detail = database.search_details(name)

    if detail:
        print("\n Employee found!")
        print(f"Employee ID     : {detail['emp_id']}")
        print(f"Name            : {detail['name']}")
        print(f"Department      : {detail['department']}")
        print(f"Salary          : {detail['salary']}")
        print(f"Experience      : {detail['experience']}")
    else:
        print("Employee not found!")

# search employee by department
def prompt_search_department():
    department = input("Enter employee department:")
    detail = database.search_department(department)

    if detail:
        print("\n Employee found!")
        print(f"Employee ID     : {detail['emp_id']}")
        print(f"Name            : {detail['name']}")
        print(f"Department      : {detail['department']}")
        print(f"Salary          : {detail['salary']}")
        print(f"Experience      : {detail['experience']}")
    else:
        print("Employee not found!")

# Delete an employee
def prompt_delete_employee():
    name = input("Enter employee name:")
    database.delete_employee(name)

# update employee salary
def prompt_update_salary():
    name = input("Enter employee name:")
    new_salary = float(input("Enter employee salary:"))
    database.update_salary(name, new_salary)

def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_employee()
        elif user_input == 'l':
            list_employees()
        elif user_input == 's':
            prompt_search_details()
        elif user_input == 'S':
            prompt_search_department()
        elif user_input == 'd':
            prompt_delete_employee()
        elif user_input == 'p':
            prompt_update_salary()
        else:
            print("Invalid choice!")

        user_input = input(USER_CHOICE)

menu()

