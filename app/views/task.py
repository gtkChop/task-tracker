from flask import Blueprint, render_template, request
from flask.views import MethodView, View


task = Blueprint(
    'task',
    __name__,
    url_prefix='/task'
)


class TaskCreateView(MethodView):
    """
    Creates a new task
    """
    def get(self):
        pass

    def post(self):
        pass


class TaskView(MethodView):
    """
    Used to get and update task given id
    """
    def get(self):
        pass

    def post(self):
        pass


class TaskListView(View):
    """
    List all the tasks given params
    """
    def dispatch_request(self):
        pass


task.add_url_rule("/", view_func=TaskListView.as_view('task_list'))
task.add_url_rule("/new", view_func=TaskCreateView.as_view('task_create'))
task.add_url_rule("/<id>", view_func=TaskView.as_view('task_view'))
