from pydantic import BaseModel
from typing import Union
from classes.task import Task
from datetime import date

## Modelo de la clase de "tarea" para el procesamiento de fastApi
class Model_task(BaseModel):
    id: int
    description: str
    status: str
    creation_date: Union[date, None]
    update_date: Union[date, None]

    @classmethod
    def from_task(cls, task: Task):
        return cls(id=task.get_taskId(), description=task.get_description(), status=task.get_status(), creation_date=task.get_createdAt(), update_date=task.get_updatedAt())
    
class HttpTask(BaseModel):
    name: str


