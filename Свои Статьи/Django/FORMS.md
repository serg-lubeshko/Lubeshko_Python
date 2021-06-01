# FORMS

https://djbook.ru/examples/57/

https://tproger.ru/translations/django-orm-tips/

**Форма** в HTML – это набор элементов в `<form>...</form>`, которые позволяют пользователю вводить текст, выбирать опции, изменять объекты и конторолы страницы, и так далее, а потом отправлять эту информацию на сервер.

Формы Django проверяют тип каждого поля класса (в модели нет), чтобы выяснить, имеет ли поле тип django.forms.fields.Field.

Класс формы, связанной c моделью, является производным от класса **ModelForm** из модуля `django.forms.`

```python
from django.forms import ModelForm 
from .models import Bb 
class BbForm (ModelForm): 
	class Meta: 
    model = Bb 
	fields = (’title’, ’content’, ’price’, ’rubric’)
```

Обрабатывать формы, связанные с моделью, можно в контроллерах-функциях. Но лучше использовать высокоуровневый контроллер-класс

```python
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from bboard.forms import BbForm

class BbCreateView(CreateView):
    template_name = 'bboard/create.htm.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics']  = Rubric.objects.all()
        return context


```



