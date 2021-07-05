import logging
from concurrent.futures import ThreadPoolExecutor
from grpc import server
import task_pb2, task_pb2_grpc

from random import seed
from random import randint
# seed random number generator
seed(1)


class TaskapiImpl:
    """'Implementation of the Taskapi service"""

       
    def __init__(self):
        # TODO: initialise attributes to store our tasks.
        self.tasks = task_pb2.Tasks()
        #Id values are randomly generated and checked at each new Task add, so that deleted Id s can be used later(at delete task id will be deleted form this id list)
        self.id_list=[0] #List keeps the Id values that exists(0 is not given as an ID)
     
        pass

    def addTask(self, request, context):
        logging.info(f"adding task {request.description}")
        # TODO: implement this!
        ##Generate a new Id(A randoly generated number
        id_num=0
        while(id_num in self.id_list):
            id_num=randint(0, 1000)
        self.id_list.append(id_num)       
        
      ##Add to task list
        self.tasks.tasks.append(task_pb2.Task(id=id_num,description=request.description))
             
      ##Return Id to client
        return task_pb2.Id(id=id_num)
        

    def delTask(self, request, context):
        logging.info(f"deleting task {request.id}")
        # TODO: implement this!
        
         ##Delete the Task from tasks
        deleted_task=task_pb2.Task()
       
        for item in self.tasks.tasks:
            if(item.id==request.id):
                deleted_task=item 
                self.tasks.tasks.remove(item)
                break
                
       ##Delete id from id list
        self.id_list.remove(request.id)
        
       ##Returning the deleted Task
        return deleted_task
        
        

    def listTasks(self, request, context):
        logging.info("returning task list")
        # TODO: implement this!
        return self.tasks
         
         
         
         

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    with ThreadPoolExecutor(max_workers=1) as pool:
        taskserver = server(pool)
        task_pb2_grpc.add_TaskapiServicer_to_server(TaskapiImpl(), taskserver)
        taskserver.add_insecure_port("[::]:50051")
        try:
            taskserver.start()
            logging.info("Taskapi ready to serve requests")
            taskserver.wait_for_termination()
        except:
            logging.info("Shutting down server")
            taskserver.stop(None)
