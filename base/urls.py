from django.urls import path
from .views import StudentLogin, StudentLogout, LibrarianLogin, LibrarianLogout, WelcomePage, LibrarianPage, StudentEnter, StudentRemove, BookEnter, BookRemove, BookAssign, BookReturn, StudentPage

urlpatterns = [
    path('', WelcomePage, name = 'WelcomePage'),
    path('studentlogin', StudentLogin, name = 'StudentLogin'),
    path('studentlogout', StudentLogout, name = 'StudentLogout'),
    path('librarianlogin', LibrarianLogin, name = 'LibrarianLogin'),
    path('librarian', LibrarianPage, name = 'Librarian'),
    path('student', StudentPage, name = 'Student'),
    path('studententer', StudentEnter, name = 'StudentEnter'),
    path('studentremove', StudentRemove, name = 'StudentRemove'),
    path('bookenter', BookEnter, name = 'BookEnter'),
    path('bookremove', BookRemove, name = 'BookRemove'),
    path('assignbook', BookAssign, name = 'BookAssign'),
    path('returnbook', BookReturn, name = 'BookReturn'),
    path('librarianlogout', LibrarianLogout, name = 'LibrarianLogout')
]
