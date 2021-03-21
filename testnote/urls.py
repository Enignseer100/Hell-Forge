from django.urls import path
from . import views

app_name = 'testnote'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:board_id>/', views.detail, name='detail'),
    path('comment/create/<int:board_id>/', views.comment_create, name='comment_create'),      #특정 게시글의 댓글이므로 board_id  sjaruwna
    path('board/create/', views.board_create, name='board_create'),
]