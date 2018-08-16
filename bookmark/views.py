from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# view 두 종류 : 함수형, 클래스형
# 클래스형 : 자주 쓰는 기능을 상속받아서 간단하게 생성

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import Bookmark
from django.urls import reverse_lazy

# List View
class BookmarkListView(ListView):
    model = Bookmark
    # 클래스형 뷰는 기본적으로 렌더링할 템플릿 파일이 지정 되어있습니다.
    # bookmark/bookmark_list.html

class BookmarkCreateView(CreateView):
    model = Bookmark # 입력화면에 출력된 form tag를 자동으로 만들어줌
    # _form : create, update
    # default : form
    template_name_suffix = '_create'
    # 입력받을 필드 목록
    fields = ['site_name','url']
    # get_absolute_url
    success_url = reverse_lazy('list')

class BookmarkUpdateView(UpdateView):

    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:list')

class BookmarkDetailView(DetailView):
    model = Bookmark

# def list(request):
#     return HttpResponse("List Page")
#
# def write(request):
#     return HttpResponse("write Django")
#
# def update(request):
#     return HttpResponse("update Django")
#
# def delete(request):
#     return HttpResponse("delete Django")