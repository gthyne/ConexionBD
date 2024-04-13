import os
import daoConnection as dao
from features.city import city_service
from features.job import job_service
from features.employee import employee_service

os.system('cls')
conex = dao.Connection("localhost", "root", "", "registrodb")
conex.connect()

def main():
    op = 0
    while op != 6:
        main_menu()
        op = int(input("Ingrese su opcion: "))
        if op == 1:
            city_operations()
        elif op == 2:
            job_operations()
        elif op == 3:
            employee_operations()
        elif op == 6:
            print("Hasta luego")
            break
        else:
            print("Opcion no valida. Intentelo de nuevo.")

def main_menu():
    print("--------- Menu Principal ---------")
    print("1. Ciudad")
    print("2. Trabajo")
    print("3. Empleado")
    print("6. Salir")
    print("-----------------------------------")

def city_operations():
    print("--------- Operaciones de Ciudad ---------")
    print("1. Insertar ciudad")
    print("2. Mostrar ciudad")
    print("-----------------------------------------")
    option = int(input("Ingrese su opcion: "))

    if option == 1:
        city_service.insertarCiudad(conex)
    elif option == 2:
        city_service.mostrar(conex)

def job_operations():
    print("--------- Operaciones de Trabajo ---------")
    print("1. Insertar trabajo")
    print("2. Mostrar trabajo")
    print("-------------------------------------------")
    option = int(input("Ingrese su opcion: "))

    if option == 1:
        job_service.insertarTrabajo(conex)
    elif option == 2:
        job_service.mostrar(conex)

def employee_operations():
    print("--------- Operaciones de Empleado ---------")
    print("1. Insertar empleado")
    print("2. Mostrar empleado")
    print("--------------------------------------------")
    option = int(input("Ingrese su opcion: "))
    
    if option == 1:
        employee_service.insertarEmpleado(conex)
    elif option == 2:
        employee_service.mostrar(conex)

if __name__ == "__main__":
    main()

"""


#instanciar modelo
nombre = input ("ingrese el nombre: ")
city =c.city(nombre,1)
city1 = c.City("Managua", 1)
city2 = c.City("León", 1)
city3 = c.City("Granada", 1)
city4 = c.City("Masaya", 1)
city5 = c.City("Estelí", 1)
city6 = c.City("Jinotepe", 1)

#instanciar dao
daoCity = dao.DaoCity(conex)
#insertar
daoCity.insert(city1)
daoCity.insert(city2)
daoCity.insert(city3)
daoCity.insert(city4)
daoCity.insert(city5)
daoCity.insert(city6)

#consultar
cities = daoCity.get_all()
for city in cities:
    print(city)
"""


