from django.db import models


class Book(models.Model):
    authfname = models.CharField(max_length=200)
    authlname = models.CharField(max_length=200)
    bname = models.CharField(max_length=200)
    book_year = models.IntegerField()

    def __str__(self):
        return self.bname

books = Book.objects.all()
for book in books:
    print(book)














