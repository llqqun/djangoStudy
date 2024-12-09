from django.urls import path
from book.urls import urlpatterns
from . import views
urlpatterns = [
    path("", views.index, name='home'),
    path("contain", views.advanced, name='advanced'),
]