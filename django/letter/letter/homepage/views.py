from django.shortcuts import render,redirect
from django.http import HttpResponse
from homepage.models  import mail, Author
from .forms import LetterForm


def index(request):

    return render(request, 'index.html')

def letter_view(request):
    if request.method == "POST":
        form = LetterForm(request.POST)
        if form.is_valid():
            # 폼이 유효하면 사연을 처리 (예: 데이터베이스에 저장)
            story = form.cleaned_data['story']
            # 예: 데이터베이스에 저장하거나 다른 처리를 할 수 있습니다.
            return redirect('finish')  # 'finish' 페이지로 리디렉션
        else:
            # 폼에 오류가 있으면 폼을 다시 렌더링
            return render(request, 'letter.html', {'form': form})

    else:
        # GET 요청 시 빈 폼을 렌더링
        form = LetterForm()
        return render(request, 'letter.html', {'form': form})

def homepage_view(request):
    return render(request, 'homepage.html') #커밋이 안되네
#커밋이 안돼!!!

def finish_view(request):
    if request.method == "POST":
        # 사용자가 입력한 사연을 받아오기
        story = request.POST.get('story')
        if not story:
            # 사연이 비어 있으면 에러 메시지
            return render(request, 'letter.html', {'form': form, 'error': '사연을 작성해주세요.'})
        
        # 사연을 처리하는 코드 (예: 데이터베이스에 저장)
        # 예시로 임시로 출력
        return HttpResponse(f"사연이 제출되었습니다: {story}")

    return render(request, 'letter.html')  # GET 요청 시 폼 렌더링

def submit_view(request):
    if request.method == "POST":
        # 폼 데이터 처리 (예: 저장, 유효성 검사 등)
        return redirect('finish')  # 폼 제출 후 'finish' 페이지로 리디렉션
    return render(request, 'your_form_template.html') 