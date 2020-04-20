from django.urls import path
from .views import home, TodoItemCreateView, TodoItemDeleteView, TodoItemUpdateView, updatedone

app_name = 'todoapp'

urlpatterns = [
    path('home/', home.as_view(), name = 'home-url'),
    path('create/', TodoItemCreateView.as_view(), name = 'create'),
    path('update/<pk>/', TodoItemUpdateView.as_view(), name = 'update'),
    path('delete/<pk>', TodoItemDeleteView, name = 'delete'),
    path('update-done/<pk>',updatedone,name="update-done"),

]
