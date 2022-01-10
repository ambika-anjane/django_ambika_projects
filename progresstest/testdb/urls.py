from django.urls import path
from .api import SourcesCreateApi,SourcesApi,SourcesUpdateApi,SourcesDeleteApi
urlpatterns = [
    path('api',SourcesApi.as_view()),
    path('api/create',SourcesCreateApi.as_view()),
    path('api/<int:pk>',SourcesUpdateApi.as_view()),
    path('api/<int:pk>/delete',SourcesDeleteApi.as_view()),
]
