"""
URL configuration for shaadi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user.views import home,signupview,signinview,userprofileview,profilefilterview,filtershow,profiledetails,add_like,showlikedview,view_chat,subscribe,profileeditview,preferenceview,preferenceshowview,Logout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path("signup",signupview.as_view(),name="sup"),
    path('',signinview.as_view(),name='signinu'),
    path('profile',userprofileview,name='upro'),
    path('editprofile',profileeditview.as_view(),name='useredit'),
    path('filter',profilefilterview.as_view(),name='profilefilter'),
    path('preferedprofile',preferenceview.as_view(),name="preference"),
    path('prefrenceresult',preferenceshowview,name='prefrenceresult'),
    path('filterresult',filtershow.as_view(),name='fushow'),
    path('users/<int:id>/', profiledetails, name='user-detail'),
    path('addlike/<int:id>/',add_like,name='addlike'),
    path('likedlist',showlikedview,name='likedlist'),
    path('chat/<int:recipient_id>/', view_chat, name='view_chat'),
    path('subscribe',subscribe.as_view(),name='subscribe'),
    path('logout',Logout.as_view(),name='logout'),
   
    



    # path('chat/<int:id>',ChatView.as_view(),name='chatfun')
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
