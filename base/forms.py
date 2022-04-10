from django.forms import ModelForm
from .models import Student, Librarian, Book

class StudentLoginForm(ModelForm):
    class Meta:
        model = Student
        fields = ['reg_no', 'password']

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        exclude = ['max_assignable']

class StudentRemoveForm(ModelForm):
    class Meta:
        model = Student
        fields = ['reg_no']

class LibrarianForm(ModelForm):
    class Meta:
        model = Librarian
        fields = "__all__"

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

class BookRemoveForm(ModelForm):
    class Meta:
        model = Book
        fields = ['book_id']
