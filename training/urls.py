from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('post/<int:id>/',views.po_list,name='po_list')
]