from django.urls import path

from .views import im_post, im_get, im_get_by_uuid_good, im_delete, goods_post_paginate, getPartGoods, \
    getDescriptionParts, good_post, goods_deleteAll

urlpatterns = [
    path('upload/', im_post, name='im-post'),
    path('download/', im_get, name='im-get'),
    path('downloadByUuidGood/<str:uuid_good>', im_get_by_uuid_good, name='im-get-by-uuid-good'),
    path('delete/<str:uuid>', im_delete, name='im-delete'),
    path('goodsPaginate/', goods_post_paginate, name='goods-paginate'),
    path('getPartGoods/', getPartGoods, name='goods-part'),
    path('getDescriptionParts', getDescriptionParts, name='get-description-parts'),
    path('uploadGood/', good_post, name='good - parts'),
    path('deleteAllGoods/', goods_deleteAll, name='goods - deleteAll')
]
