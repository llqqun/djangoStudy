from django.urls import path
from . import views
app_name = "book"
urlpatterns = [
    # 127.0.0:8000/book/detail?id=1
    path("detail", views.book_detail, name="book_detail"),
    # 127.0.0:8000/book/detail/1
    # 路径参数设置，可以定义参数类型，比如这里定义了int类型，那么路径参数只能是数字，否则返回404
    path("detail/<int:book_id>", views.book_detail_path, name="book_detail_path"),
]