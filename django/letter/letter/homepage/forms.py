from django import forms

class LetterForm(forms.Form):
    story = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': '사연을 여기에 작성하세요.', 'rows': 4, 'cols': 50}),
        required=True
    )
