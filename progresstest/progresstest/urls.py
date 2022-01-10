"""progresstest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include, re_path 
from testdb.views import SourcesViewSet,UserViewSet,GroupViewSet
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from testdb.serializers import UserSerializer, GroupSerializer, SourcesSerializers
from testdb.api import SourcesCreateApi


# Serializers define the API representation.



router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'sources', SourcesViewSet)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('source/',include('testdb.urls'))
    
]       
'''
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
]

'''



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

#You can now open the API in your browser at http://127.0.0.1:8000/, and view your new 'users' API. If you use the login control in the top right corner you'll also be able to add, create and delete users from the system.



    

