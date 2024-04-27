
from django.urls import path
from studentapp import views

urlpatterns = [

    path('', views.StudentListView.as_view(), name='student_list'),
    
    path('list/', views.StudentListView.as_view(), name='student_list'),

    path('create/', views.StudentCreateView.as_view(), name='student_create'),

    path('<int:pk>/update/', views.StudentUpdateView.as_view(), name='student_update'),

    path('<int:pk>/delete/', views.StudentDeleteView.as_view(), name='student_delete'),

    path('<int:pk>/detail/', views.StudentDetailView.as_view(), name='student_detail'),

]
