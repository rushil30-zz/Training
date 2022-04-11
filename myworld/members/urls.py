from django.urls import path
#from django.conf.urls import patterns, url
from . import views
from members.views import StaticView
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('add/addrecord/', views.add_record, name='addrecord'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path('testing_queries/', views.testing, name='testing_queries'),
    path('static/', StaticView.as_view(), name='static'),
    path('sendemail/' , views.sendEmail, name='sendemail'),
    path('email-attachment/', views.simple_send_mail, name='email-attachment'),
    # path(('connection/', views.login, TemplateView.as_view(template_name = 'login.html'))),
    # path('login/', views.login, name = 'login'),
    # # patterns('members.views', url(r'^connection/', TemplateView.as_view(template_name = 'login.html'))),
    # path('profile/', views.SaveProfile,TemplateView.as_view(template_name = 'profile.html')),
    path('saved/', views.SaveProfile, name = 'saved'),
]

