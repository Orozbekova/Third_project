from django.urls import path

from music.views import *

urlpatterns = [
    path('',ListCreateView.as_view()),
    path('<int:pk>/',DeleteUpdateRetriveView.as_view()),
]