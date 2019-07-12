import json

from datetime import datetime
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import View

from .models import BookInfo, HeroInfo
class IndexView(View):

    def get(self, request):
        context = {
            'city': '北京',
        }
        return render(request, 'index.html', context)


# REST API
# GET /books/  获取所有图书信息
# GET /books/<pk>/ 获取单一图书
# POST /books/ 新增图书
# PUT /books/<pk>/ 更新图书
# DELETE /books/<pk>/ 删除图书

class BooksAPIView(View):

    def get(self, request):
        books = BookInfo.objects.all()
        # 转换
        books_list = []
        for book in books:
            books_list.append({
                "id": book.id,
                "btitle": book.btitle,
                "bpub_date": book.bpub_date.strftime("%Y-%m-%d"),
                "bread": book.bread,
                "bcomment": book.bcomment,
                "image": book.image.url if book.image else ''
            })

        return JsonResponse(books_list, safe=False)

    def post(self, request):
        # POST 新增图书
        json_bytes = request.body
        json_str = json_bytes.decode()
        req_date = json.loads(json_str)

        # 省略校验参数
        book = BookInfo.objects.create(
            btitle=req_date.get('btitle'),
            bpub_date=datetime.strptime(req_date.get('bpub_date'), '%Y-%m-%d').date()
        )

        # 转换
        book_dict = {
                "id": book.id,
                "btitle": book.btitle,
                "bpub_date": book.bpub_date.strftime("%Y-%m-%d"),
                "bread": book.bread,
                "bcomment": book.bcomment,
                "image": book.image.url if book.image else ''
            }

        return JsonResponse(book_dict, status=201)


class BookAPIView(View):
    def get(self, request, pk):
        # GET /books/<pk>/ 获取单一图书
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        # 转换
        book_dict = {
            "id": book.id,
            "btitle": book.btitle,
            "bpub_date": book.bpub_date.strftime("%Y-%m-%d"),
            "bread": book.bread,
            "bcomment": book.bcomment,
            "image": book.image.url if book.image else ''
        }

        return JsonResponse(book_dict)

    def put(self, request, pk):
        # 更新图书
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        json_bytes = request.body
        json_str = json_bytes.decode()
        req_date = json.loads(json_str)

        # 省略校验参数
        book.btitle = req_date.get('btitle')
        book.bpub_date = datetime.strptime(req_date.get('bpub_date'), '%Y-%m-%d').date()
        book.save()

        # 转换
        book_dict = {
            "id": book.id,
            "btitle": book.btitle,
            "bpub_date": book.bpub_date.strftime("%Y-%m-%d"),
            "bread": book.bread,
            "bcomment": book.bcomment,
            "image": book.image.url if book.image else ''
        }

        return JsonResponse(book_dict, status=201)

    def delete(self, request, pk):
        # 删除
        try:
            book = BookInfo.objects.get(pk=pk)
        except BookInfo.DoesNotExist:
            return HttpResponse(status=404)

        book.delete()
        return HttpResponse(status=204)