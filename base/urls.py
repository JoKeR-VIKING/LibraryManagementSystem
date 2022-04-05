from django.urls import path
from .views import StudentLogin, LibrarianLogin, LibrarianLogout, WelcomePage, LibrarianPage, StudentEnter, StudentRemove, BookEnter, BookRemove

urlpatterns = [
    path('', WelcomePage, name = 'WelcomePage'),
    path('studentlogin', StudentLogin, name = 'StudentLogin'),
    path('librarianlogin', LibrarianLogin, name = 'LibrarianLogin'),
    path('librarian', LibrarianPage, name = 'Librarian'),
    path('studententer', StudentEnter, name = 'StudentEnter'),
    path('studentremove', StudentRemove, name = 'StudentRemove'),
    path('bookenter', BookEnter, name = 'BookEnter'),
    path('bookremove', BookRemove, name = 'BookRemove'),
    path('librarianlogout', LibrarianLogout, name = 'LibrarianLogout')
]
