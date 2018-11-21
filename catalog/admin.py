from django.contrib import admin
from catalog.models import Author, Genre, Book, BookInstance, Language

# Register your models here.
admin.site.register(Genre)
admin.site.register(Language)


class BookInline(admin.TabularInline):
    model = Book


# Register the admin class with the associated model
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'date_of_birth', 'date_of_death']
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [
        BookInline
    ]


class BookInstanceInline(admin.TabularInline):
    model = BookInstance


# Register the admin class with the associated model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'display_genre', 'language']
    inlines = [
        BookInstanceInline,
    ]


# Register the admin class with the associated model
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ['book', 'status', 'borrower', 'due_back', 'id']
    list_filter = ['status', 'due_back']
    fieldsets = (
        ('General Information', {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        })
    )
