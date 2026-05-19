from django.urls import path
from . import views

urlpatterns = [
    path('make/', views.makeFormation, name='makeFormation'),
    path('modify/<int:id>/', views.mdifyFormation, name='modifyFormation'),
    path('remove/<int:id>/', views.removeFormation, name='removeFormation'),
]
