from rest_framework import generics
from rest_framework.response import Response
from testdb.serializers import SourcesSerializers
from testdb.models import Sources


 
class SourcesCreateApi(generics.CreateAPIView):
    serializer_class = SourcesSerializers
    
    def get_queryset(self) :
        user = self.request.user
        return Sources.objects.filter(name=user)
        
class SourcesApi(generics.ListAPIView):
    queryset = Sources.objects.all()
    serializer_class = SourcesSerializers
class SourcesUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Sources.objects.all()
    serializer_class = SourcesSerializers
class SourcesDeleteApi(generics.DestroyAPIView):
    queryset = Sources.objects.all()
    serializer_class = SourcesSerializers
    
    '''qs = Sources.objects.all()
    print(SourcesSerializers(qs, many=True).data)

def get_queryset(self):
    return self.name
    '''