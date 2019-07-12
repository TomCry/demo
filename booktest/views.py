__author__ = 'enzyme'
__date__ = '2019/7/11 7:24 PM'

import json
from django.http import HttpResponse, JsonResponse
from .models import BookInfo, HeroInfo
from rest_framework.views import APIView
from .serializers import BookInfoSerializer, HeroInfoSerializer
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny, BasePermission

# class BookListAPIView(APIView):
#     def get(self, request):
#         # 数据库查询
#         queryset = BookInfo.objects.all()
#         # 构建序列化器对象进行序列化操作
#         serializer = BookInfoSerializer(queryset, many=True)
#         serializer.data
#
#         return Response(serializer.data)

# GET /books/
# class BookListAPIView(GenericAPIView):
#     queryset = BookInfo.objects.all()
#     serializer_class = BookInfoSerializer
#
#     def get(self, request):
#         qs = self.get_queryset()
#         # 数据库查询
#         serializer = self.get_serializer(qs, many=True)
#         return Response(serializer.data)

from rest_framework import mixins

# class BookListAPIView(mixins.ListModelMixin, GenericAPIView):
#     queryset = BookInfo.objects.all()
#     serializer_class = BookInfoSerializer
#
#     def get(self, request):
#         return self.list(request)
# class BookListAPIView(ListAPIView):
#     queryset = BookInfo.objects.all()
#     serializer_class = BookInfoSerializer

# 视图集
from rest_framework.viewsets import GenericViewSet


class BookInfoViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer


# GET /books/<pk>/
class BookDetailAPIView(GenericAPIView):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

    def get(self, request, pk):
        book = self.get_object()
        serializer = self.get_serializer(book)
        return Response(serializer.data)


from rest_framework.decorators import action
from .serializers import BookReadSerialzer


class MyPermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        return False


class BookInfoViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = BookInfo.objects.all()
    # serializer_class = BookInfoSerializer
    permission_classes = [MyPermission]

    def get_serializer_class(self):
        # 重写提供不同的序列化器
        if self.action == 'read':
            return BookReadSerialzer
        else:
            return BookInfoSerializer

    # def get_permissions(self):
    #     if self.action == 'read':
    #         return [IsAuthenticated()]
    #     else:
    #         return [AllowAny()]

    # detail为False 表示不需要处理具体的BookInfo对象
    @action(methods=['get'], detail=False)
    def latest(self, request):
        """
        返回最新的图书信息
        """
        book = BookInfo.objects.latest('id')
        serializer = self.get_serializer(book)
        return Response(serializer.data)

    # detail为True，表示要处理具体与pk主键对应的BookInfo对象
    @action(methods=['put'], detail=True)
    def read(self, request, pk):
        """
        修改图书的阅读量数据
        """
        book = self.get_object()
        book.bread = request.data.get('read')
        serializer = self.get_serializer(instance=book, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # serializer = self.get_serializer(book)
        return Response(serializer.data)
