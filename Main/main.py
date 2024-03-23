import os
import daoConnection as dao
import clases as c

os.system('cls')
conex = dao.Connection("localhost", "root", "", "dbregisters")
conex.connect()

def insertarciudad():
    nombre = input("nombre ciudad")
    ciudad = c.city(nombre, 1)
    daoCity = dao.daocity(conex)
    cities = daoCity.get_all()
    for city in cities:
        print (city)
    #insertar
    daoCity.insert(ciudad)

    def Menu():
        print("1,insertar ciudad")
        print("2,editar ciudad")
        print("3,mostrar ciudad")
        print("4,Eliminar ciudad")
        print("5,buscar  ciudad")
        print("6,salir")


    def main():
        op = 0
        while(op !=6):
            menu()
        opcion = int(input("dime tu opcion")) 
        if (opcion == 1):
            insertarciudad()
            os.system("pausa")









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
