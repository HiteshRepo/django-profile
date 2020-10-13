
from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('<int:project_id>', views.projectdetails, name='projectdetail'),
]
