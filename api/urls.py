from django.urls import path, include
from rest_framework import routers, urlpatterns
from .views import  CreateUserView, ListUserView, LoginUserView, LostArticleViewSet

router = routers.DefaultRouter()
router.register('lostaritcle', LostArticleViewSet)


urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create'),
    path('users/', ListUserView.as_view(), name='users'),
    path('loginuser/', LoginUserView.as_view(), name='loginuser'),
    path('', include(router.urls)),
]