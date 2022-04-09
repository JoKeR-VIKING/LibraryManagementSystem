from django.db import models

class Student(models.Model):
    name = models.CharField(max_length = 100)
    year = models.CharField(max_length = 100)
    division = models.CharField(max_length = 100)
    roll_no = models.CharField(max_length = 100)
    reg_no = models.CharField(max_length = 100)
    password = models.CharField(max_length = 15)
    max_assignable = models.IntegerField(default = 2)
    assigned_books = models.CharField(max_length = 500, null = True, blank = True)

class Librarian(models.Model):
    name = models.CharField(max_length = 100, blank = True, null = True)
    user_id = models.CharField(max_length = 25)
    id_no = models.CharField(max_length = 7)

class Book(models.Model):
    book_id = models.CharField(max_length = 100)
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    category = models.CharField(max_length = 100)
    amount = models.IntegerField(default = 1)

class History(models.Model):
    reg_no = models.CharField(max_length = 100)
    history = models.JSONField(default = dict)