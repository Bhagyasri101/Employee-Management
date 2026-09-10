from fastapi import FastAPI

app = FastAPI()

details = []

@app.post("/details")
def insert_details(emp_id : str, name : str, department : str, salary : float, experience : int):

    for detail in details:
        if detail["emp_id"] == emp_id:
            return {
                "message": "Employee ID already exists!"
            }
        
    detail = {
        "emp_id": emp_id,
        "name": name,
        "department": department,
        "salary": salary,
        "experience": experience
    }

    details.append(detail)

    return {
        "message": "Employee details added successfully!",
        "detail": detail
    }

@app.get("/details")
def get_all_employee():
    return details

@app.get("/details/search/name")
def search_details(name : str):
    for detail in details:
            if detail["name"].lower() == name.lower():
                return detail
    return {"message" : "Employee not found!"}

@app.get("/details/search/department")
def search_department(department : str):
     result = []

     for detail in details:
          if detail["department"].lower() == department.lower():
               result.append(detail)

     if len(result) == 0:
          return {"message": "Employee not found!"}

     return result

@app.delete("/details")
def delete_employee(name : str):
     for detail in details:
             if detail["name"].lower() == name.lower():
                 details.remove(detail)
                 return {"message" : "Employee details detailed successfully!"}
        
     return {"message" : "Employee not found!"}

@app.put("/details/salary")
def update_salary(name : str, new_salary : float):
     detail = search_details(name)
     
     if detail:
          detail["salary"] = new_salary
          return {
               "message" : "Employee salary is updated successfully!",
               "detail" : detail
          }
     return {"message" : "Employee salary is not found!"}



