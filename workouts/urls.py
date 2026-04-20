from django.urls import path
from workouts import views

urlpatterns = [
    path('', views.workout_list, name='workout_list'),
    path('create/', views.workout_create, name='workout_create'),
    path('<int:pk>/add-exercises/', views.workout_add_exercises, name='workout_add_exercises'),
    path('<int:pk>/', views.workout_detail, name='workout_detail'),
    path('<int:pk>/edit/', views.workout_edit, name='workout_edit'),
    path('<int:pk>/complete/', views.workout_complete, name='workout_complete'),
    path('<int:pk>/delete/', views.workout_delete, name='workout_delete'),

]
