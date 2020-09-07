from django.urls import path
from . import views
urlpatterns=[
    path("hello_world",views.hello_world),
    path("content",views.Article_content),
    path("index",views.get_index_page),
    path("detail",views.get_detail_page),
]