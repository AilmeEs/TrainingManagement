from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('post/<int:id>/',views.po_list,name='po_list')

#     path('post/list/', views.PostList.as_view(),name='post_list'),
    path('post/detail/<pk>/',views.PostDetail.as_view(),name='post_detail'),
    path('post/delete/<int:id>/', views.post_delete, name='post_delete'),
    path('register/',views.register,name='register'),

]