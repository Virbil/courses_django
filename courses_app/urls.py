from django.urls import path
from . import views

urlpatterns = [
    path('', views.courses),
    path('courses/destroy/<int:course_id>', views.delete_course, name="delete_course"),
]