from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('quiz/', views.quiz, name='quiz'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('result/', views.result, name='result'),
    path('export_participants_xlsx/', views.export_participants_xlsx, name='export_participants_xlsx'),
    path('export_participants_pdf/', views.export_participants_pdf, name='export_participants_pdf'),
    path('study/', views.study, name='study'),
]

