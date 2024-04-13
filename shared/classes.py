class City:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def __str__(self):
        return self.name
    
class Job:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def __str__(self):
        return self.name
    
class Employee:
    def __init__(self, nombre=None, ciudad_id=None, job_id=None, salary=None, status=None):
        self.nombre = nombre
        self.ciudad_id = ciudad_id
        self.job_id = job_id
        self.salary = salary
        self.status = status

    def get_id(self):
        return self.id

    def get_nombre(self):
        return self.nombre

    def get_ciudad_id(self):
        return self.ciudad_id

    def get_job_id(self):
        return self.job_id

    def get_salary(self):
        return self.salary

    def get_status(self):
        return self.status
