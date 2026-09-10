

details = []

def insert_details(emp_id, name, department, salary, experience):

    detail = {"emp_id" : emp_id, "name" : name, "department" : department, "salary" : salary, "experience" : experience}

    details.append(detail)

    print("Employee details added successfully!")

def get_all_employee():
    return details

def search_details(name):

    for detail in details:
        if detail["name"].lower() == name.lower():
            return detail
    return None

def search_department(department):

    for detail in details:
        if detail["department"].lower() == department.lower():
            return detail
    return None

def delete_employee(name):

    for detail in details:
        if detail["name"].lower() == name.lower():
            details.remove(detail)
            print("Employee is detailed successfully!")
        return
    print("Employee not found!")

def update_salary(name, new_salary):
    detail = search_details(name)

    if detail:
        detail["salary"] = new_salary
        print("Employee salary is updated successfully!")
    else:
        print("Employee salary is not found!")





