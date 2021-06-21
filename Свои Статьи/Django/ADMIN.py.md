# ADMIN.py

```python
admin.site.register(Bb) #регистрируем модель
class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published')
    list_display_links = ('title', 'content')
    
admin.site.register(Bb, BbAdmin)
```

Класс редактора объявляется как производный от класса `ModelAdmin` из модуля `django. cont rib. admin.`

| Атрибуты класса   | Описание                                                     |
| ----------------- | ------------------------------------------------------------ |
| list display      | последовательность имен полей, которые должны выводиться в списке записей |
| list_dispiay_link | последовательность имен полей, которые должны быть преобразованы в гиперссылки, ведущие на страницу правки записи; |
| search_field      | последовательность имен полей, по которым должна выпол­няться фильтрация. |
| mark_safe         | отрисовывает строку в html                                   |
|                   |                                                              |
|                   |                                                              |
|                   |                                                              |
|                   |                                                              |
|                   |                                                              |

Делаем выпадающее меню в админке, где таблица БД == категории объекта

```python
from django.contrib import admin
from .models import *
from django import forms


class NotebookCategoryChoiseField(forms.ModelChoiceField):
    pass


class NoteBookAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return NotebookCategoryChoiseField(Category.objects.filter(slug='Noutbuki'))
        return super().formfield_for_foreignkey(self, db_field, request, **kwargs)
```

