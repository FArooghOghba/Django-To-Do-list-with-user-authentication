from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'base'

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='base:login'), name='logout'),
    path('register/', views.RegisterPageFormView.as_view(), name='register'),
    path('', views.TaskListView.as_view(), name='tasks'),
    path('task/<int:pk>/', views.TaskDetailView.as_view(), name='task'),
    path('new_task/', views.TaskCreateView.as_view(), name='task_create'),
    path('update_task/<int:pk>/', views.TaskUpdateView.as_view(), name='task_update'),
    path('delete_task/<int:pk>/', views.TaskDeleteView.as_view(), name='task_delete'),
]
