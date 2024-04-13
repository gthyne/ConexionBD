class DaoEmployee:
    def __init__(self, connection):
        self.connection = connection
    
    def get_all(self):
        query = 'SELECT * FROM employees'
        return self.connection.execute_read_query(query, ())
    
    def get_by_id(self, id):
        query = 'SELECT * FROM employees WHERE id = %s'
        return self.connection.execute_read_query(query, (id,))
    
    def insert(self, employee):
        query = 'INSERT INTO employees (nombre, ciudad_id, job_id, salary, status) VALUES (%s, %s, %s, %s, %s)'
        return self.connection.execute_query(query, (employee.nombre, employee.ciudad_id, employee.job_id, employee.salary, employee.status))
    
    def update(self, employee):
        query = 'UPDATE employees SET nombre = %s, ciudad_id = %s, job_id = %s, salary = %s, status = %s WHERE id = %s'
        return self.connection.execute_query(query, (employee.nombre, employee.ciudad_id, employee.job_id, employee.salary, employee.status, employee.id))
    
    def delete(self, id):
        query = 'DELETE FROM employees WHERE id = %s'
        return self.connection.execute_query(query, (id,))
