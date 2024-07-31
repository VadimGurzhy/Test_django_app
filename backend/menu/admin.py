from django.contrib import admin

from . models import Menu, Item_menu


@admin.register(Menu)
class Menu(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Item_menu)
class Item(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent', 'menu')
    list_filter = ('menu', )
    fieldsets = (
        (None, {
            'fields': (('menu', 'parent'), 'name')
        }),
    )
