from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegisterRegularUser.as_view()),
    path('register/regular/', views.RegisterRegularUser.as_view()),
    path('register/admin/', views.RegisterAdministratorUser.as_view()),
]