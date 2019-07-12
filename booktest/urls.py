__author__ = 'enzyme'
__date__ = '2019/7/10 1:57 PM'

from django.conf.urls import url, include

from . import views

# urlpatterns = [
#     # url(r'^booktest/$', views_old.IndexView.as_view()),
#     # url(r'^books/$', views_old.BooksAPIView.as_view()),
#     # url(r'^books/(?P<pk>\d+)/$', views.BookDetailAPIView.as_view()),
#     # url(r'books/$', views.BookListAPIView.as_view()),
#     url(r'^books/(?P<pk>\d+)/$', views.BookInfoViewSet.as_view({'get': 'retrieve'})),
#     url(r'books/$', views.BookInfoViewSet.as_view({'get': 'list'})),
#     url(r'books/latest/$', views.BookInfoViewSet.as_view({'get': 'latest'})),
#     url(r'books/(?P<pk>\d+)/read/$', views.BookInfoViewSet.as_view({'put': 'read'})),
# ]
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', views.BookInfoViewSet, base_name='book_base')

urlpatterns = [
    url(r'', include(router.urls))
]



# urlpatterns += router.urls
