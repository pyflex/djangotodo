from django.urls import path
from . import views
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns




urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<list_id>', views.delete, name='delete'),
    path('cross_off/<list_id>', views.cross_off, name='cross_off'),
    path('edit/<list_id>', views.edit, name='edit')
]

urlpatterns += staticfiles_urlpatterns()
