# URLS.py

```python
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("shop/", include("sales_manager.urls"))
]
```

Для того, что бы загруженные файлы можно было просматривать (а не загружать) на сайте необходимо создать соответствующий маршрут, который будет указывать на загруженные файлы. Для этого используется функция static из модуля `from django.conf.urls.static import static`. Эта функция создаст маршрут по которому маршрутизатор передаст при запросе файлов управление специальному контроллеру Django, который и отдаст нам файл для просмотра. Этот маршрут мы используем только в режиме DEBUG.  Для этого перейдем в корневой URLS.py и пропишем в   `urlpatterns` необходимый код (см. URLS.py)

```python
#корневой urls.py
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
    
#MEDIA_URL -  константа, которую мы создали в settings.py

```

