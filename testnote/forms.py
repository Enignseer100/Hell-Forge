from django import forms
from testnote.models import Board       #모델을 상속받음 = DB에 연결됨

class BoardForm(forms.ModelForm):
    class Meta:                         #DB연결시 Meta class 필수
        model = Board
        fields = ['subject', 'content']  #제목, 내용
        labels = {
            'subject' : '제목',
            'content' : '내용',
        }