import os

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
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


@api_view(http_method_names=['GET'])
def getDescriptionParts(request):
    response_data = {}
    import json

    from django.core import serializers
    try:
        query_set = Good.objects.values_list('uuid_part').distinct()
        data = []
        for el in query_set:
            tp = tuple(el)
            if tp.__sizeof__() > 0:
                data.append(tp[0])

        response_data['success'] = True
        response_data['message'] = 'OK'
        response_data['data'] = data
    except Exception as err:
        response_data['success'] = False
        response_data['message'] = err.__str__()
        response_data['data'] = ''

    return JsonResponse(response_data, safe=True)


@api_view(http_method_names=['GET'])
def getPartGoods(request, uuid_part, pre_uuid_parts):
    try:
        Good.objects.filter(uuid_part=pre_uuid_parts).delete()
    except Exception as err:
        print(err)

    response_data = {}

    try:
        query_set = Good.objects.filter(uuid_part=uuid_part)
        data = GoodSerializer(query_set, many=True)
        response_data['success'] = True
        response_data['message'] = 'OK'
        response_data['data'] = data.data
    except Exception as err:
        response_data['success'] = False
        response_data['message'] = err.__str__()
        response_data['data'] = ''

    return JsonResponse(response_data, safe=True)
