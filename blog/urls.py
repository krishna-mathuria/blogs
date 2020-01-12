from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('addblog2',views.addblog),
    path('submit',views.submit)
 #   path('addblog2', views.AddblogView.as_view(), name='addblog

]