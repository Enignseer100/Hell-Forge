from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Board, Comment
from django.utils import timezone       #현재시간
from .forms import BoardForm
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    # 입력 인자
    page = request.GET.get('page', 1)

    # 조회
    board_list = Board.objects.order_by('-create_date')    
    
    # 페이징 처리   
    paginator = Paginator(board_list, 5)
    page_obj = paginator.get_page(page)

    context = {'board_list': page_obj}
    #context = {'board_list' : board_list}
    #return HttpResponse("testnote 에 오신것을 환영합니다!");
    return render(request, 'testnote/board_list.html', context)

def detail(request, board_id):
    board = Board.objects.get(id=board_id)
    context = {'board': board}
    return render(request, 'testnote/board_detail.html', context)

def comment_create(request, board_id):
    board = Board.objects.get(id=board_id)
    #comment = Comment(board=board, content=request.POST.get('content'), create_date=timezone.now()) 데이터 저장시 사용하는 기본문법
    #comment.save()
    #return redirect('testnote:detail', board_id=board_id)
    board.comment_set.create(content=request.POST.get('content'), create_date=timezone.now())     #foreign_key로 연결된 모델의 경우 Comment 모델에서 값을 가져오지 않고 한줄로 압축 가능
    return redirect('testnote:detail', board_id=board.id)

def board_create(request):
    if request.method == 'POST':                    #post로 들어왔을 경우 게시글 등록
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)         #저장하되 commit x(밑 구문에서 등록일자 세팅 고려)
            board.create_date = timezone.now()
            board.save()
            return redirect('testnote:index')
    else:                                       #get으로 들어왔을 경우 등록하지않고 작성한 내용 그대로 넘기기
        form = BoardForm()
    return render(request, 'testnote/board_form.html', {'form':form})