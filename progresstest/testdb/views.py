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
