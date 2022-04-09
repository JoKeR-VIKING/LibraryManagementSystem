from django.contrib import admin
from .models import Student, Librarian, Book, History

admin.site.register(Student)
admin.site.register(Librarian)
admin.site.register(Book)
admin.site.register(History)