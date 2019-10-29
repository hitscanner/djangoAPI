from django.contrib import admin
# Diary 추가
from .models import Book,Diary

admin.site.register(Book)
admin.site.register(Diary)