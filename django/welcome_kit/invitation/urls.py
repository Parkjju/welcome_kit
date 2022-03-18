from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'invitation'

urlpatterns = [
    path('', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('home',views.home, name ='home'),
    path('main',views.main, name ='main'),

    path('roadmap_FE',views.roadmap_FE, name ='roadmap_FE'),
    path('roadmap_BE',views.roadmap_BE, name ='roadmap_BE'),
    path('roadmap_PMD',views.roadmap_PMD, name ='roadmap_PMD'),
    path('roadmap_today',views.roadmap_today, name ='roadmap_today'),

    path('doctor',views.doctor, name ='doctor'),

    path('bingo1',views.bingo1, name ='bingo1'),
    path('bingo2',views.bingo2, name ='bingo2'),

    path('agit',views.agit, name ='agit'),
]