from . import employee_dao as Dao
from shared.classes import Employee

def insertarEmpleado(conex):
    nombre = input("nombre empleado: ")
    ciudad_id = int(input("id de la ciudad: "))
    job_id = int(input("id del trabajo: "))
    salary = float(input("salario: "))
    status = input("estado: ")
    
    empleado = Employee(nombre=nombre, ciudad_id=ciudad_id, job_id=job_id, salary=salary, status=status)
    daoemployee = Dao.DaoEmployee(conex)
    daoemployee.insert(empleado)

def mostrar(conex):
    daoemployee = Dao.DaoEmployee(conex)
    cities = daoemployee.get_all()
    for job in cities:
        print(job)