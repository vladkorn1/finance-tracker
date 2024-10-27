from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    #path('categories/', views.categories, name='categories'),
    #path('create/', views.create, name='create'),
    #path('categories/<int:pk>', views.CategoryDetailView.as_view(), name='details_view'),
    #path('categories/<int:pk>/update', views.CategoryUpdateView.as_view(), name='update_view'),
    #path('categories/<int:pk>/delete', views.CategoryDeleteView.as_view(), name='delete_view')
]
