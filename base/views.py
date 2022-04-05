from django.shortcuts import render, redirect
from .forms import StudentForm, LibrarianForm, StudentRemoveForm, BookForm, BookRemoveForm
from .models import Student, Librarian, Book

def StudentLogin(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
    else:
        form = StudentForm()

    return render(request, 'base/student_list.html')

def WelcomePage(request):
    return render(request, 'base/home.html')

def LibrarianLogin(request):
    if request.method == "POST":
        form = LibrarianForm(request.POST)

        if form.is_valid():
            if Librarian.objects.filter(user_id = form.cleaned_data['user_id'], id_no = form.cleaned_data['id_no']).exists():
                request.session["user_id"] = form.cleaned_data['user_id']
                return redirect('/librarian')

        return render(request, 'base/librarian_list.html')
    else:
        form = LibrarianForm()
        return render(request, 'base/librarian_list.html')

def LibrarianLogout(request):
    if "user_id" not in request.session:
        return redirect('/')

    del request.session['user_id']
    return redirect('/')

def LibrarianPage(request):
    if "user_id" in request.session:
        return render(request, 'base/librarian_page.html')
    else:
        return redirect('/')

def StudentEnter(request):
    if "user_id" not in request.session:
        return redirect('/')

    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            if not Student.objects.filter(reg_no = form.cleaned_data['reg_no']).exists():
                name = form.cleaned_data['name']
                year = form.cleaned_data['year']
                division = form.cleaned_data['division']
                roll_no = form.cleaned_data['roll_no']
                reg_no = form.cleaned_data['reg_no']

                Student.objects.create(name = name, year = year, division = division, roll_no = roll_no, reg_no = reg_no)
            else:
                print("Record exists")

        return redirect('/librarian')
    else:
        form = StudentForm()
        return render(request, 'base/create_list.html')

def StudentRemove(request):
    if "user_id" not in request.session:
        return redirect('/')

    if request.method == "POST":
        form = StudentRemoveForm(request.POST)

        if form.is_valid():
            if Student.objects.filter(reg_no = form.cleaned_data['reg_no']).exists():
                reg_no = form.cleaned_data['reg_no']

                Student.objects.filter(reg_no = reg_no).delete()
            else:
                print("Record does not exist")

        return redirect('/librarian')
    else:
        form = StudentForm()
        return render(request, 'base/create_list.html')

def BookEnter(request):
    if "user_id" not in request.session:
        return redirect('/')

    if request.method == "POST":
        form = BookForm(request.POST)

        if form.is_valid():
            if not Book.objects.filter(book_id = form.cleaned_data['book_id']).exists():
                book_id = form.cleaned_data['book_id']
                title = form.cleaned_data['title']
                author = form.cleaned_data['author']
                category = form.cleaned_data['category']

                Book.objects.create(book_id = book_id, title = title, author = author, category = category)
            else:
                print("Record exists")

        return redirect('/librarian')
    else:
        form = BookForm()
        return render(request, 'base/create_list.html')

def BookRemove(request):
    if "user_id" not in request.session:
        return redirect('/')

    if request.method == "POST":
        form = BookRemoveForm(request.POST)

        if form.is_valid():
            if Book.objects.filter(book_id = form.cleaned_data['book_id']).exists():
                book_id = form.cleaned_data['book_id']

                Book.objects.filter(book_id = book_id).delete()
            else:
                print("Record does not exist")

        return redirect('/librarian')
    else:
        form = BookForm()
        return render(request, 'base/create_list.html')