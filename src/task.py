class Task:


    def __init__(self, taskId, description, status, createdAt, updatedAt):
        self.__taskId = taskId
        self.__description = description
        self.__status = status
        self.__createdAt = createdAt
        self.__updatedAt = updatedAt
    
    def __str__(self):
        return f"id: {self.__taskId}. descripción: {self.__description}. status: {self.__status}. se creó en: {self.__createdAt}. se actualizó en: {self.updatedAt} "


    ## GETTERS Y SETTERS ----------- DIVISION DEL PAPU
    def get_taskId(self):
        return self.__taskId
    
    def get_description(self):
        return self.__description
    
    def get_status(self):
        return self.__status
    
    def get_createdAt(self):
        return self.__createdAt
    
    def get_updatedAt(self):
        return self.__updatedAt
    ## GETTERS Y SETTERS ----------- DIVISION DEL PAPU


    def sumIdOne(self):
        return self.__taskId + 1