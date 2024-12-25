from django.shortcuts import render, redirect
from homepage.models import mail
from .forms import LetterForm

def index(request):
    return render(request, 'index.html')

def letter_view(request):
    if request.method == "POST":
        form = LetterForm(request.POST)
        if form.is_valid():
            # 폼이 유효하면 사연을 처리 (모델에 저장)
            story = form.cleaned_data['story']
            # 새로운 mail 객체를 생성하여 데이터베이스에 저장
            new_mail = mail(detail=story)
            new_mail.save()  # 데이터베이스에 저장

            return redirect('finish')  # 'finish' 페이지로 리디렉션
        else:
            # 폼에 오류가 있으면 폼을 다시 렌더링
            return render(request, 'letter.html', {'form': form})

    else:
        # GET 요청 시 빈 폼을 렌더링
        form = LetterForm()
        return render(request, 'letter.html', {'form': form})

def homepage_view(request):
    return render(request, 'homepage.html')

def finish_view(request):
    return render(request, 'finish.html')  # 사연 제출 후 완료 페이지
