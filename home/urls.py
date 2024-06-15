from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('welcome/', views.welcome, name='welcome'),
    path('about/', views.welcome, name='about'),
    path('question/<int:question_id>/', views.question_view, name='question'),
    path('results/', views.results_view, name='results'),
]
