from django.contrib import admin
from books.models import Student, Category, Books


class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'cpf', 'birth_date' , 'city', 'email', 'tel', 'registration_date', 'book']
    search_fields = ['id', 'name']
    list_display_links = ['name']
    list_filter = ['registration_date']
    list_editable = ['tel']

class BooksAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at', 'category']
    search_fields = ['id', 'name']
    list_display_links = ['name']
    list_filter = ['category']
    list_editable = ['category']

admin.site.register(Student, StudentAdmin)
admin.site.register(Category)
admin.site.register(Books, BooksAdmin)
