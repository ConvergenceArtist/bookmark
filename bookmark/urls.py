from django.contrib import admin
from django.urls import path

# 2차 URL

# name 의 목적 template  'list/' 의 목적 뷰를 연결하기 위해
from  .views import *
# app_name => 네임스페이스 // url 이름을 가지고 패턴을 찾고자 할 때 namespace를 사용하려면 app_name이 필수!
app_name = 'bookmark'
urlpatterns = [

    # 함수형뷰 : 함수형 이름만
    # 클래스형 뷰 : 클래스이름.as_view()

    path('', BookmarkListView.as_view(), name='list'),
    path('write/', BookmarkCreateView.as_view(), name='write'),
    path('update/<int:pk>', BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', BookmarkDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>', BookmarkDetailView.as_view(), name='detail'),
    # re_path(regexp,,),
    # url(regexp, ?, ?)
]

