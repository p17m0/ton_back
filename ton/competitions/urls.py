from django.urls import path
from . import views

urlpatterns = [
    path('competitions/', views.competition_list),
    path('competitions/<int:pk>/', views.competition_list),
]
