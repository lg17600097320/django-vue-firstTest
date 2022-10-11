from django.shortcuts import render
from  rest_framework.viewsets import ModelViewSet
from  .serializers import CommentSerializers
from  .models import Comment
from  .permissions import  IsOwnerOrReadOnly
# Create your views here.

class CommentModelViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(auther=self.request.user)