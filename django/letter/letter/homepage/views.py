from django.shortcuts import render, redirect
from homepage.models import Mail

def index(request):
    return render(request, 'index.html')

def letter_view(request):
    if request.method == "POST":
        # POST 요청으로 들어온 데이터를 가져오기
        story = request.POST.get('story')
        if story:  # 내용이 비어있지 않으면 저장
            new_mail = Mail(detail=story)
            new_mail.save()  # 데이터베이스에 저장
            return redirect('finish')  # 저장 후 'finish' 페이지로 리디렉션
        else:
            # 내용이 비어있으면 에러 메시지와 함께 다시 렌더링
            return render(request, 'letter.html', {'error': '내용을 입력해주세요.'})
    return render(request, 'letter.html')  # GET 요청 시 템플릿 렌더링

def homepage_view(request):
    return render(request, 'homepage.html')

def finish_view(request):
    return render(request, 'finish.html')  # 사연 제출 후 완료 페이지

