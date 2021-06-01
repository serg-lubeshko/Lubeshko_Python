# views.py

Обрабатывать **формы**, связанные с моделью, можно в контроллерах-функциях. Но лучше использовать высокоуровневый контроллер-класс `Createview` из модуля `django.views.generic.edit.`

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

## django.views.generic.edit Createview

|                     |                                                              |
| ------------------- | ------------------------------------------------------------ |
| template_name       | путь к файлу шаблона, создающего страницу с формой           |
| form_class          | ссылка на класс формы, связанной с моделью;                  |
| success_url         | интернет-адрес для перенаправления после успешного сохране­ния данных (в нашем случае это адрес главной страницы). |
| get_context_data () | Поскольку на каждой странице сайта должен выводиться перечень рубрик переопределили метод. ФОРМИРУЕТ КОНТЕКСТ ШАБЛОНА |
| reverse_lazy        | Из модуля django.urls принимает имя маршрута и значе­ния всех входящих в маршрут URL-параметров (если они там есть). |
|                     |                                                              |
|                     |                                                              |
|                     |                                                              |
|                     |                                                              |

