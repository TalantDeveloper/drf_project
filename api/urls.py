from django.urls import path
from . import views


urlpatterns = [
    path('', views.getData, name='get-data'),
    path('add/', views.addItem, name='add-data'),

]
