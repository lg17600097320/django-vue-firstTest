from django.shortcuts import render
from  rest_framework.viewsets import ModelViewSet
from  django.contrib.auth.models import User
from  .serializers import UserRegisterSerializers,UserDetailSerializers
from  rest_framework.permissions import AllowAny,IsAuthenticatedOrReadOnly
from  .permissions import IsSelfOrReadOnly
from  rest_framework.decorators import action
from  rest_framework.response import  Response
from  rest_framework import status
# Create your views here.

class  UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class =  UserRegisterSerializers
    lookup_field = 'username'

    @action(detail=True,methods=['GET'])
    def info(self,request,username=None):
        queryset =  User.objects.get(username=username)
        serializers = UserDetailSerializers(queryset,many=True)
        return  Response(serializers.data,status=status.HTTP_200_OK)

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticatedOrReadOnly,IsSelfOrReadOnly]
        return  super().get_permissions()
