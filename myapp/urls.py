from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeacherListView, ReceptionTemplateView, HomeView,StudentRegisterView,YunalishlarListView
from . views import *
urlpatterns=[
    path('', HomeView.as_view(), name='home'),
    path('teachers/', TeacherListView.as_view(), name='teacher-list'),
    path('reception/', ReceptionTemplateView.as_view(), name='reception'),
    path('student-register/', StudentRegisterView.as_view(), name='student-register'),
    path('yunalishlar/', YunalishlarListView.as_view(), name='yunalishlar'),
    path('teachers/<int:pk>/', TeacherDetailView.as_view(), name='teacher-detail'),
    path('yunalishlar/<int:pk>/', YunalishDetailView.as_view(), name='yunalish-detail'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news-detail'),

]