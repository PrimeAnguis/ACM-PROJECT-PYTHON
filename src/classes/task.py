from datetime import date

## Clase de tarea

class Task:
    def __init__(self, taskId: int, description: str, status: str, updated_at: date|None):
        self._task_id = taskId 
        self._description = description
        self._status = status
        self._created_at = date.today()
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
            
    def set_status(self, current_status: str):

        if current_status == "NOT DONE":
            self._status = "UN-FINISHED"
        
        if current_status == "UN-FINISHED":
            self._status = "FINISHED"

    def set_updatedAt(self):
        self._updated_at = date.today()

    
    ## GETTERS Y SETTERS ----------- DIVISION 

