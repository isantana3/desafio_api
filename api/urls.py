from django.urls import path
from api import views

urlpatterns = [
    path('soma/', views.soma, name ='soma'),
    path('sub/', views.sub, name = 'sub'),
    path('multi/', views.multi, name = 'multi'),
    path('div/', views.div, name = 'div'),
    path('hist/', views.hist, name = 'hist'),
]