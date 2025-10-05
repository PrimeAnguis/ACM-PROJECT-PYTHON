from task import Task

newTask = Task(15, "Terminar el coso de fisica", False, "15/08/2025", "20/09/2030" )

print("La fecha de creación de la tarea es:", newTask.get_createdAt())
print(newTask.sumIdOne())