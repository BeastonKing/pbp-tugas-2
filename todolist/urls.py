from django.urls import path
from todolist.views import add_task, add_task_ajax, login_user, logout_user, register, show_as_json, show_todolist, show_todolist_ajax

app_name = 'todolist'

urlpatterns = [
    # path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', add_task, name='add_task'),
    path('json/', show_as_json, name='show_as_json'),
    path('', show_todolist_ajax, name='show_todolist_ajax'),
    path('add', add_task_ajax, name='add_task_ajax'),
]