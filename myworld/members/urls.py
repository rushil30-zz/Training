from django.urls import path
# from members.models import Members
from . import views
from members.views import StaticView
from django.views.generic import ListView

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('add/addrecord/', views.addrecord, name='addrecord'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('testing_queries/', views.testing, name='testing_queries'),
    path('static/', StaticView.as_view(), name='static'),
]

