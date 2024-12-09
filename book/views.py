from django.shortcuts import render, HttpResponse

# Create your views here.

def book_detail(request):
    book_id = request.GET.get('id')
    return HttpResponse(f'书的id是{book_id}')

def book_detail_path(request, book_id):
    return HttpResponse(f'书的id是{book_id}')