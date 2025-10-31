class Task:


    def __init__(self, taskId, description, status, created_at, updated_at):
        self._task_id = taskId
        self._description = description
        self._status = status
        self._created_at = created_at
        self._updated_at = updated_at

    def __str__(self):
        return f"TAREA #: {self._task_id}. DESCRIPCIÓN: {self._description}. STATUS: {self._status}. CREADO: {self._created_at}. ACTUALIZADO: {self._updated_at}"
    

    ## GETTERS Y SETTERS ----------- DIVISION 
    def get_taskId(self):
        return self._task_id
    
    def get_description(self):
        return self._description
    
    def get_status(self):
        return self._status
    
    def get_createdAt(self):
        return self._created_at
    
    def get_updatedAt(self):
        return self._updated_at
    
    def set_taskId(self, new_id):
        self._task_id = new_id

    def set_description(self, new_description):
        self._description = new_description
        
    
    def set_status(self, new_status):
        self._status = new_status 
    
    def set_creation_date(self, new_date):
        self._created_at = new_date

    
    ## GETTERS Y SETTERS ----------- DIVISION 


