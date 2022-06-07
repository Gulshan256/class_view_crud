from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.studentList.as_view()),
    path('<int:pk>/',views.studentDetail.as_view()),
]