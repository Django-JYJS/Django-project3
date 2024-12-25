from django import forms

class LetterForm(forms.Form):
    story = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': '군 생활중 고충이나 건의사항을 여기 적어주세요.', 'rows': 20, 'cols': 100}),
        required=True
    )
