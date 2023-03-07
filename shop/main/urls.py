from django.urls import path
from .views import *

urlpatterns = [
    path('about', about),
    path('category/<int:c_id>', tasks, name='tasks'),
    path('category/task<int:task_id>/del', task_del, name='task_del'),
    path('category/task<int:task_id>', descriptions, name='desc'),
    path('add_category', add_category, name='add_c'),
    path('category/<str:category>/add_task', add_task, name='add_task'),
    path('category/<int:c_id>/del', category_del, name='c_del'),
    path('done_tasks/<int:task_id>/not_done', not_done, name='n_done'),
    path('done_tasks/delete', done_tasks_del, name='done_del'),
    path('done_tasks', done_tasks, name='d_tasks'),
    path('', index, name='home'),

]