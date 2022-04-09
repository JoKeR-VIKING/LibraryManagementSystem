from django.shortcuts import render, redirect
from django.db.models import F
from .forms import StudentLoginForm, StudentForm, LibrarianForm, StudentRemoveForm, BookForm, BookRemoveForm
from .models import Student, Librarian, Book, History
import datetime

def StudentLogin(request):
    if request.method == "POST":
        form = StudentLoginForm(request.POST)

        if form.is_valid():
            if Student.objects.filter(reg_no = form.cleaned_data['reg_no'], password = form.cleaned_data['password']).exists():
                request.session["student_id"] = form.cleaned_data['reg_no']
                return redirect('/student')
            else:
                print("Student does not exist")

        return redirect('/')
    else:
        form = StudentLoginForm()

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
                password = form.cleaned_data['password']

                Student.objects.create(name = name, year = year, division = division, roll_no = roll_no, reg_no = reg_no, password = password)
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
                amount = form.cleaned_data['amount']

                if amount == "":
                    amount = 1
                else:
                    amount = int(amount)

                Book.objects.create(book_id = book_id, title = title, author = author, category = category, amount = amount)
            else:
                print("Record exists")

        return redirect('/librarian')
    else:
        form = BookForm()
        return render(request, 'base/create_book.html')

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
        return render(request, 'base/create_book.html')

def BookAssign(request):
    if "student_id" not in request.session:
        return redirect('/')
    if "bookname" not in request.POST:
        return redirect('/student')

    err_message = ''

    if Student.objects.filter(reg_no = request.session['student_id'], max_assignable__gte = 1).exists():
        assigned_books = Student.objects.filter(reg_no = request.session['student_id']).values('assigned_books')
        for i in assigned_books:
            assigned_books = i['assigned_books']

        if assigned_books is None:
            assigned_books = ""

        Student.objects.filter(reg_no = request.session['student_id']).update(max_assignable = F('max_assignable') - 1,
                                                                            assigned_books = assigned_books + ";" + request.POST['bookname'])
        Book.objects.filter(book_id = request.POST['bookname']).update(amount = F('amount') - 1)

        if not History.objects.filter(reg_no = request.session['student_id']).exists():
            History.objects.create(reg_no = request.session['student_id'])

        newHistory = History.objects.filter(reg_no = request.session['student_id']).values('history')
        for i in newHistory:
            newHistory = i['history']

        if request.POST['bookname'] not in newHistory:
            newHistory[request.POST['bookname']] = ""

        newHistory[request.POST['bookname']] += f'1,{datetime.datetime.now().date()};'

        History.objects.filter(reg_no = request.session['student_id']).update(history = newHistory)
    else:
        print("Student with id does not exist or has run out of assign quota")

    return redirect('/student')

def BookReturn(request):
    if "student_id" not in request.session:
        return redirect('/')
    if "bookname" not in request.POST:
        return redirect('/student')

    assignedBooks = Student.objects.filter(reg_no = request.session['student_id']).values('assigned_books')
    for i in assignedBooks:
        assignedBooks = i['assigned_books']

    assignedBooks = assignedBooks.replace(';' + request.POST['bookname'], '', 1)

    Student.objects.filter(reg_no=request.session['student_id']).update(max_assignable = F('max_assignable') + 1,
                                                                        assigned_books = assignedBooks)
    Book.objects.filter(book_id = request.POST['bookname']).update(amount = F('amount') + 1)

    if not History.objects.filter(reg_no = request.session['student_id']).exists():
        History.objects.create(reg_no = request.session['student_id'])

    newHistory = History.objects.filter(reg_no = request.session['student_id']).values('history')
    for i in newHistory:
        newHistory = i['history']

    if request.POST['bookname'] not in newHistory:
        newHistory[request.POST['bookname']] = ""

    newHistory[request.POST['bookname']] += f'0,{datetime.datetime.now().date()};'

    History.objects.filter(reg_no = request.session['student_id']).update(history = newHistory)

    return redirect('/student')

def StudentPage(request):
    if "student_id" not in request.session:
        return redirect('/')

    # selecting books with amount >= 1
    allbooks = Book.objects.filter(amount__gte = 1)
    assignedBooks = Student.objects.filter(reg_no = request.session['student_id']).values('assigned_books')
    for i in assignedBooks:
        assignedBooks = i['assigned_books']

    if assignedBooks is not None and len(assignedBooks) > 0:
        assignedBooks = assignedBooks.split(';')
        assignedBooks = assignedBooks[1:]

    return render(request, 'base/student_page.html', {'allbooks' : allbooks, 'returnBooks' : assignedBooks})

def StudentLogout(request):
    if "student_id" not in request.session:
        return redirect('/student')

    del request.session['student_id']
    return redirect('/')
