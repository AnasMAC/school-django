from django.urls import path
from . import views

urlpatterns = [
    path('enroll/<int:id>/', views.enrollToFormation, name='enrollToFormation'),
]
