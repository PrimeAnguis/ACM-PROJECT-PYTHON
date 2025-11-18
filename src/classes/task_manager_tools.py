from classes.task import Task

## Clase de la lista de tareas

class Task_Manager:
    
    def __init__(self):
        
        self.task_list = []
        

    def add_task(self, newTask: Task):
        self.task_list.append(newTask)
        
    def delete_task(self, task: Task):
        self.task_list.remove(task)

    def new_task(self, name: str):
        try:
            id = len(self.task_list) + 1
            new_task = Task(id, name, "NOT DONE", None)
            self.add_task(new_task)

            return new_task
        except Exception as e:
            print(e)
            return None

    ## Busqueda y lista
    
    def list_all_tasks(self):
        return self.task_list
         
    def id_search(self, id):
        return next((task for task in self.task_list if task.get_taskId() == id), None)

    def update_task(self, task: Task):
        task_status = task.get_status()
        task.set_updatedAt()
        task.set_status(task_status)

        return task
        
    
  
    
    
