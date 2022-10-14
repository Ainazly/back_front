from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from news.models import News
from news.serializers import NewsSerializer


@api_view(['GET'])
def new_list_view(request):
    tasks = News.objects.all()
    serializer = NewsSerializer(tasks, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def detail_list_view(request, id):
    detail_list = News.objects.get(id=id)
    serializer = NewsSerializer(detail_list, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def news_create_view(request):
    serializer = NewsSerializer.get(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response({"Created": "Object is created"})


@api_view(['POST'])
def news_update_view(request, id):
    news = News.objects.get(id=id)
    serializer = NewsSerializer(instance=news, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def news_delete_view(request, id):
    news = News.objects.get(id=id)

    news.delete()
    return Response({"obj": "Delete"})

