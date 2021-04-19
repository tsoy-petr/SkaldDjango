from abc import ABC

from django.db import models
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers
from rest_framework.pagination import PageNumberPagination


class ImageGood(models.Model):
    uuid = models.CharField(primary_key=True, max_length=36)
    uuid_good = models.CharField(max_length=36)
    ext = models.CharField(max_length=20, blank=True)
    image = models.ImageField(upload_to='img/%Y/%m/%d/', blank=True)
    title = models.CharField(max_length=120, blank=True)

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete()
        super().delete()


class ImageGoodSerializer(serializers.ModelSerializer):
    image = Base64ImageField()

    class Meta:
        model = ImageGood
        fields = ('uuid', 'uuid_good', 'ext', 'image', 'title')

        def create(self, validated_data):
            uuid = validated_data.pop('uuid')
            uuid_good = validated_data.pop('uuid_good')
            ext = validated_data.pop('ext')
            image = validated_data.pop('image')
            title = validated_data.pop('title')
            return ImageGood.objects.create(uuid=uuid, uuid_good=uuid_good, ext=ext, image=image, title=title)


class Good(models.Model):
    id_uuid = models.BigAutoField(primary_key=True, auto_created=True)
    uuid = models.CharField(max_length=36, default='')
    name = models.CharField(max_length=300, default='')
    uuid_parent = models.CharField(max_length=36, default="", blank=True)
    isGroup = models.BooleanField(default=False, blank=True)
    article_number = models.CharField(max_length=50, default="", blank=True)
    uuid_part = models.CharField(max_length=36, blank=True)

    class Meta:
        unique_together = ('uuid', 'uuid_part')


class GoodPartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Good
        fields = list('uuid_part')


class GoodSerializer(serializers.ModelSerializer):
    # def __init__(self, *args, **kwargs):
    #     # Don't pass the 'fields' arg up to the superclass
    #     fields = kwargs.pop('fields', None)
    #
    #     # Instantiate the superclass normally
    #     super(GoodSerializer, self).__init__(*args, **kwargs)
    #
    #     if fields is not None:
    #         # Drop any fields that are not specified in the `fields` argument.
    #         allowed = set(fields)
    #         existing = set(self.fields)
    #         for field_name in existing - allowed:
    #             self.fields.pop(field_name)

    class Meta:
        model = Good
        fields = ('uuid', 'name', 'uuid_parent', 'isGroup', 'article_number', 'uuid_part')

        def create(self, validated_data):
            uuid = validated_data.pop('uuid')
            name = validated_data.pop('name')
            uuid_parent = validated_data.pop('uuid_parent')
            isGroup = validated_data.pop('isGroup')
            article_number = validated_data.pop('article_number')
            uuid_part = validated_data.pop('uuid_part')
            return Good.objects.create(uuid=uuid, name=name, uuid_parent=uuid_parent, isGroup=isGroup,
                                       article_number=article_number, uuid_part=uuid_part)


class ResultsSetPaginationGoods(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 100000
