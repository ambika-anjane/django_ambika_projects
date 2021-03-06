from django.shortcuts import render
from testdb.models import Teacher
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from testdb.serializers import UserSerializer, GroupSerializer, SourcesSerializers
from testdb.models import Sources


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class SourcesViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = SourcesSerializers
    permission_classes = [permissions.IsAuthenticated]



from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)



'''  
@action(methods=['delete'], detail=False)
def delete(self, request, pk, format=None):
        transformer = self.get_object(pk)
        transformer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    



# Create your views here.
def viewdisplay(request):
    tobj =  Teacher.objects.all()
    return render(request, "testdb/showteacher.html",{"data": tobj})
'''
