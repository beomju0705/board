from django import forms
from .models import Book

class DateInput(forms.DateInput):
    input_type = 'date'

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'pub_date']
        labels = {
            'title': '제목',
            'author': '저자',
            'pub_date': '출판일',
        }
        widgets = {
            'pub_date': DateInput(),
        }