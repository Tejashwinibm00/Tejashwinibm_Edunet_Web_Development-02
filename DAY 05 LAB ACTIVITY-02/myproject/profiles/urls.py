<<<<<<< HEAD
from django.urls import path

from . import views

urlpatterns = [
    #Mapping the URL '/students/' to the student_list view
    path('students/', views.student_list, name = 'student_list'),
]
=======
from django.urls import path

from . import views

urlpatterns = [
    #Mapping the URL '/students/' to the student_list view
    path('students/', views.student_list, name = 'student_list'),
]
>>>>>>> 86c0bec (Initial commit with large folder)
