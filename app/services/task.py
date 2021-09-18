from services import schema
import logging

log = logging.getLogger(__name__)

class TaskService:

    @staticmethod
    @schema.task_create_validator
    def create_task(data_dict: dict):
        pass


    @staticmethod
    def update_task(data_dict: dict):
        pass


    @staticmethod
    def get_task(task_id: int):
        pass


    @staticmethod
    def task_list(items_per_page: int, filter_dict: dict):
        pass


    @staticmethod
    def delete_task(task_id: int):
        pass
