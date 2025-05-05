from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.CharField(max_length=255)
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return self.titleppyth