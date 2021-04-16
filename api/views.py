import os

from django.views.generic import ListView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from .models import *


@api_view(http_method_names=['POST'])
def im_post(request):
    serializer = ImageGoodSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=400)


@api_view(http_method_names=['GET'])
def im_get(request):
    images = ImageGood.objects.all()
    data = ImageGoodSerializer(images, many=True)
    return Response(data.data)


@api_view(http_method_names=['GET'])
def im_get_by_uuid_good(request, uuid_good):
    images = ImageGood.objects.filter(uuid_good=uuid_good)
    data = ImageGoodSerializer(images, many=True)
    return Response(data.data)


@api_view(http_method_names=['GET'])
def im_delete(request, uuid):
    try:
        imageObject = list(ImageGood.objects.filter(uuid=uuid))
        for im in imageObject:
            try:
                path = im.image.path
                if os.path.exists(path):
                    os.remove(path)
            except Exception as err:
                print(err)
    except Exception as err:
        print(err)

    ImageGood.objects.filter(uuid=uuid).delete()

    return Response('OK')


@api_view(http_method_names=['GET'])
def goods_post_paginate(request):
    paginator = PageNumberPagination()
    query_set = Good.objects.all()
    context = paginator.paginate_queryset(query_set, request)
    serializer = GoodSerializer(context, many=True)
    return paginator.get_paginated_response(serializer.data)

