from django.urls import path
from . import views

urlpatterns = [
    path('manage', views.UrlManagerView.as_view()),
    path('detail/<str:short_url>/', views.UrlDetailView.as_view()),
]