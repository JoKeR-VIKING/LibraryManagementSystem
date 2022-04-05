from django.contrib import admin
from .models import Student, Librarian, Book

admin.site.register(Student)
admin.site.register(Librarian)
admin.site.register(Book)