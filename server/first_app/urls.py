from django.urls import path
from . import views

# NO LEADING SLASHES
urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.new),
    path('create', views.create),
    path('15',views.show),
    path('edit', views.edit),
    path('destroy', views.destroy),
]