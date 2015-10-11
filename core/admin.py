from django.contrib import admin
from core import models

# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    pass


class BookAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Author, AuthorAdmin)
admin.site.register(models.Book, AuthorAdmin)

