from datetime import date

class Task_Manager:
    
    def __init__(self):
        
        self.task_list = []

    def add_task(self, newTask):
        self.task_list.append(newTask)
        
    def delete_task(self, task):
        self.task_list.remove(task)

    ## TASK LISTING CONVENTIONS
    
    def list_all_tasks(self):
        return "\n".join(str(task) for task in self.task_list)
        
    def list_all_inprogress(self):
        in_progress = [str(task) for task in self.task_list if getattr(task, "status", None) == "in progress"]
        return "\n".join(in_progress) if in_progress else "No hay tareas en progreso."
        

    def list_all_done(self):
        done = [str(task) for task in self.task_list if getattr(task, "status", None) == "done"]
        return "\n".join(done) if done else "No hay tareas completadas."


    def list_all_undone(self):
        undone = [str(task) for task in self.task_list if getattr(task, "status", None) == "not done"]
        return "\n".join(undone) if undone else "No hay tareas no iniciadas."
    
    def id_search(self, id):
        return next((task for task in self.task_list if task.get_taskId() == id), None)
    
    ## TASK LISTING CONVENTIONS
    
    def new_task_creation_protocol(self):

        today = date.today()
        new_id = int(input("Coloca un numero identificatorio. (Puedes revisar las tareas y sus numeros identificatorios mas tarde.) #: "))
        new_description = str(input("¿Que quieres recordar?:\n"))

        new_task_status = "not done"
        new_task_creation_date = today 
        new_task_updated_date = None

        attributes = (new_id, new_description, new_task_status, new_task_creation_date, new_task_updated_date)

        return attributes

    
