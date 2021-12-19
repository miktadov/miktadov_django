from django.contrib import admin
from .models import MyForm


class MyFormAdm(admin.ModelAdmin):
    list_display = ('data', 'name', 'comm', 'mess', 'colled')
    list_display_links = ('data', )
    list_filter = ('data', 'colled')
    list_editable = ('colled', )


admin.site.register(MyForm, MyFormAdm)