from django.urls import path

from . import views

urlpatterns = [
    path('category/', views.CategoryViewSet.as_view(
        {'get': 'list', 'post': 'create'}
    )),
    path('movie/', views.MovieViewSet.as_view(
        {'get': 'list', 'post': 'create'}
    )),

]