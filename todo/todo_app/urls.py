from . import views
from django.urls import path

urlpatterns = [
    path('', views.add, name='add'),
    path('delete<int:taskid>/', views.delete, name='delete'),
    path('update<int:id>/', views.update, name='update'),
    path('cbvhome/', views.list_view.as_view(), name='cbvhome'),
    path('cbvdetails/<int:pk>/', views.detail_view.as_view(), name='cbvdetails'),
    path('cbvupdate/<int:pk>/', views.update_view.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.delete_view.as_view(), name='cbvdelete'),

]
