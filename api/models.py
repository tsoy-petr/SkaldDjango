import os

from django.db import models
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers


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
    uuid = models.CharField(primary_key=True, max_length=36)
    name = models.CharField(max_length=300)
    uuid_parent = models.CharField(primary_key=True, max_length=36)
