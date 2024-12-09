from datetime import datetime

from django.shortcuts import render

# Create your views here.
def index(request):
    user_Info = { "name": "John Doe", "age": 30 }
    content = "   This is a test"
    # 列表 爱好
    hobbies = ["reading", "swimming", "programming"]

    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
            self.birthday = datetime.now()

    books = [
        { "title": '三国演义', "author": '罗贯中'},
        { "title": '水浒传', "author": '施耐庵'},
        { "title": '西游记', "author": '吴承恩'},
        { "title": '红楼梦', "author": '曹雪芹'}
    ]

    context = {
        "user": user_Info,
        "content": content,
        "hobbies": hobbies,
        "person": Person("小明", 30),
        "books": books
    }
    return render(request, 'home.html', context=context)

def advanced(request):
    user_Info = {"name": "John Doe", "age": 30}
    content = "   This is a test"
    # 列表 爱好
    hobbies = ["reading", "swimming", "programming"]

    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age
            self.birthday = datetime.now()

    books = [
        {"title": '三国演义', "author": '罗贯中'},
        {"title": '水浒传', "author": '施耐庵'},
        {"title": '西游记', "author": '吴承恩'},
        {"title": '红楼梦', "author": '曹雪芹'}
    ]

    context = {
        "user": user_Info,
        "content": content,
        "hobbies": hobbies,
        "person": Person("小明", 30),
        "books": books,
        "title": '模板高级使用'
    }
    return render(request, 'advanced.html', context=context)