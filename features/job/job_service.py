from . import job_dao as Dao
from shared.classes import Job

def insertarTrabajo(conex):
    nombre = input("nombre trabajo ")
    ciudad = Job(nombre, 1)
    daojob = Dao.DaoJob(conex)
    daojob.insert(ciudad)

def mostrar(conex):
    daojob = Dao.DaoJob(conex)
    cities = daojob.get_all()
    for job in cities:
        print(job)