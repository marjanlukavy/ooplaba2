from django.urls import path, include
from .views import DogAPIView,DogDetails,GenericAPIView,DogViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('dog-api', DogViewSet, basename='dog')



urlpatterns = [
    path('/', include(router.urls)),
    path('<int:pk>', include(router.urls)),
    path('dog-api/', DogAPIView.as_view()),
    path('dog-api/<int:id>/', DogDetails.as_view()),
    path('generic/dog-api/<int:id>/', GenericAPIView.as_view()),
]
