
from django.urls import path
# from rest_framework import views
# from rest_framework.urlpatterns import format_suffix_patterns
#
#
from blog import views

urlpatterns = [
    path('f/',views.ListView,name='function'),
    path('cl/',views.MyView.as_view(),name= 'class based'),
    path('subcl/', views.MyViewChild.as_view(), name='child class'),
    path('hf/',views.HomeFun,name ='function'),
    path('hc/',views.HomeClass.as_view(),name= 'class based home html'),
    path('af/',views.about_func,name ='function'),
    path('ac/',views.AboutClassView.as_view(),name='class about'),
    path('cf/',views.contactfun,name ='function'),
    # path('api/',views.Post_detail),
    #     path('Post/<int:pk>/', views.PostDetail.as_view()),
]
#
# # urlpatterns = format_suffix_patterns(urlpatterns)
