"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path, reverse
from django.http import HttpResponse
def index(request):
    # 模块化路由时，进行reverse操作需要添加对应的命名空间
    # 不同参数类型路径处理方式不同
    print(reverse('book:book_detail') + f'?id={123}')
    print(reverse('book:book_detail_path', kwargs={ "book_id": 321 }))
    return HttpResponse("首页")

urlpatterns = [
    path("", index, name='home'),
    path("book/", include("book.urls")),
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
    path("tem/", include("tem_demo.urls")),
    path("sql/", include("sql_app.urls")),
]
