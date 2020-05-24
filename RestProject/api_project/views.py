from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import Dog
from .serializers import DogsSerializer
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import  get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics,mixins,viewsets,status
import urllib.request
from .container import Container
from .ioc_class import das
import json
class DogViewSet(viewsets.ViewSet):
    def list(self, request):
        articles = Dog.objects.all()
        serializer = DogsSerializer(articles, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = DogsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Dog.objects.all()
        article = get_object_or_404(queryset, pk=pk)
        serializer = DogsSerializer(article)
        return Response(serializer.data)


    def update(self, reqeust,pk=None):
        article = Dog.objects.get(pk=pk)
        serializer = DogsSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin,
             mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class = DogsSerializer
    queryset = Dog.objects.all()
    lookup_field = 'id'
    def get(self, request, id):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self,request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)




class DogAPIView(APIView):
    def get(self, request):
        articles = Dog.objects.all()
        serializer = DogsSerializer(articles, many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = DogsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)


class DogDetails(APIView):
    def get_object(self, id):
        container = Container()
        a_file = open("dog_api_json.json", "w")
        json.dump(das(container.api_connection()), a_file)
        a_file.close()
        try:
            return Dog.objects.get(id=id)
        except Dog.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        article = self.get_object(id)
        serializer = DogsSerializer(article)
        return Response(serializer.data)

    def put(self, request,id):
        article = self.get_object(id)
        serializer = DogsSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        article = self.get_object(id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


