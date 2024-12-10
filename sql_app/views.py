from django.shortcuts import HttpResponse
from django.db import connection
from .models import User
# Create your views here.
# 数据库操作演示
def index(request):
    # 简单查询数据库
    # cursor = connection.cursor()
    # cursor.execute("select * from demo")
    # rows = cursor.fetchall()
    # for row in rows:
    #     print(row)
    # return HttpResponse(rows)

    # 插入数据
    # rows = User.objects.create(name="小红", age=18, sex=1)
    # print(rows)

    # ORM 保存
    # obj = User(name="小明", age=18, sex=1)
    # obj.save()

    # 修改
    # obj = User.objects.get(id=3)
    # obj.name = "小王"
    # obj.save()

    # ORM 查询所有
    rows = User.objects.all()
    for row in rows:
        print(row)

    # ORM 过滤查找
    # rows = User.objects.filter(name="小明")
    # for row in rows:
    #     print(row)

    # 单个查找
    # try:
    #     row = User.objects.get(id=10)
    #     print(row)
    # except User.DoesNotExist:
    #     print("用户不存在")

    # 删除操作
    # rows = User.objects.filter(id=2).delete()
    # print(rows)
    return HttpResponse(f"操作成功")