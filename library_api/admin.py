from django.contrib import admin

from library_api.models import Book, Author

# Register your models here.
admin.site.register(Book)

admin.site.register(Author)
