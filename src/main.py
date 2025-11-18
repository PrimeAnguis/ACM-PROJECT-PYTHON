from fastapi import FastAPI, HTTPException
from classes.task_manager_tools import Task_Manager
from py_dantic_schemes.task_mod import Model_task, HttpTask



app = FastAPI(title="Manager de tareas")
manager = Task_Manager()


# Leer datos
@app.get('/tasks')
def get_tasks():
    list_tasks = manager.list_all_tasks()

    map_iterable_task = map(lambda x: Model_task.from_task(x), list_tasks)

    return list(map_iterable_task)

@app.get('/tasks/{id}')
def get_tasks(task_id: int):

    if manager.id_search(task_id) == None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada.")
    
    return manager.id_search(task_id)

# Crear datos
@app.post('/tasks')
def add_task(task: HttpTask):
    new_task = manager.new_task(task.name)

    return Model_task.from_task(new_task)

# Actualizar datos
@app.put('/tasks/{id}')
def update_task(id: int,):

    if manager.id_search(id) == None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada.")
    
    found_task = manager.id_search(id)
    updated_task = manager.update_task(found_task)
    return Model_task.from_task(updated_task)

# Borrar datos

@app.delete('/tasks/{id}')
def delete_task(id: int):
    task_to_delete = manager.id_search(id)
    manager.delete_task(task_to_delete)

