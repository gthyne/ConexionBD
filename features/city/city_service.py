from . import city_dao as Dao
from shared.classes import City

def insertarCiudad(conex):
    nombre = input("nombre ciudad ")
    ciudad = City(nombre, 1)
    daoCity = Dao.DaoCity(conex)
    daoCity.insert(ciudad)

def mostrar(conex):
    daoCity = Dao.DaoCity(conex)
    cities = daoCity.get_all()
    for city in cities:
        print(city)





        