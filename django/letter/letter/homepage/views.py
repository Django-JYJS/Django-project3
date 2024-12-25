from django.shortcuts import render, redirect
from homepage.models import Mail
from .forms import LetterForm

def index(request):
    return render(request, 'index.html')

def letter_view(request):
    if request.method == "POST":
        form = LetterForm(request.POST)
        if form.is_valid():
            story = form.cleaned_data['story']
            new_mail = Mail(detail=story)
            new_mail.save()
            return redirect('finish')
        else:
            return render(request, 'letter.html', {'form': form})
    else:
        form = LetterForm()
        return render(request, 'letter.html', {'form': form})

def homepage_view(request):
    return render(request, 'homepage.html')

def finish_view(request):
    return render(request, 'finish.html')  # 사연 제출 후 완료 페이지

