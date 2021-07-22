from django.urls import path

from . import views

app_name = 'university'
urlpatterns = [
    path('', views.UniversityList.as_view(), name='university-list'),
    path('<int:pk>/', views.UniversityDetail.as_view(), name='university-detail'),

    path('student/', views.StudentList.as_view(), name='student-list'),
    path('student/<int:pk>/', views.StudentDetail.as_view(), name='student-detail'),
]
