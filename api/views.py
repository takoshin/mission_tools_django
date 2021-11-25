from django.shortcuts import render
from rest_framework import status, permissions, generics, viewsets
from .serializers import UserSerializer, LostArticleSerializer
from rest_framework.response import Response
from .models import User, LostArticle

class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

class ListUserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    
    def get_object(self):
        return self.request.user
    
    def update(self, requst, *args, **kwargs):
        response = {'message': 'PUT method is not allowed'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

class LostArticleViewSet(viewsets.ModelViewSet):
    queryset = LostArticle.objects.all()
    serializer_class = LostArticleSerializer

    def perform_create(self, serializer):
        serializer.save()

    def partial_update(self, request, *args, **kwargs):
        response = {'message': 'PATCH method is not allowed'}
        return Response(response, status=status.HTTP_400_BAD_REQUEST)