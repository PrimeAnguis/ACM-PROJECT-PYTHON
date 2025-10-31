from task_manager_tools import Task_Manager
from task import Task




def main():
    running = True
    new_manager = Task_Manager()

    print("Bienvenido/a al Task Manager.")

    while running:

        choice_int = int(input("Crea una tarea. Si ya tienes una, puedes revisarlas también: \n\n Coloca un numero: \n 1: Añade una tarea. \n 2: Actualiza una tarea. \n 3: Borra una tarea. \n 4: Revisa las tareas ya programadas  \n"))
        match choice_int:
            case 1:
                
                new_task = Task(*new_manager.new_task_creation_protocol())
                new_manager.add_task(new_task)
                print(f"Tarea #{new_task.get_taskId()} ha sido guardada con exito.")
                    
            case 2:

                print(new_manager.list_all_tasks())
                print("\n\n")
                id_input = int(input("Elige una tarea para modificar. \n\n IDENTIFICADOR: # "))
                task_found = new_manager.id_search(id_input) 
                new_status = str(input("Coloca el nuevo status: "))
                task_found.set_status(new_status)
                
            case 3:

                print(new_manager.list_all_tasks())
                print("\n\n")
                id_input = int(input("Elige una tarea para borrar. \n\n IDENTIFICADOR: # "))
                task_found = new_manager.id_search(id_input) 
                new_manager.delete_task(task_found)
            
            case 4:

                print(new_manager.list_all_tasks())
                ## Para la siguiente versión, hacer las divisiones de tareas entre sus estados.
                

            case _:
                exit(0)
                

    

if __name__ == "__main__":
    main()


## El programa aun no tiene implementación de JSON, las tareas tampoco pueden guardarse aun.