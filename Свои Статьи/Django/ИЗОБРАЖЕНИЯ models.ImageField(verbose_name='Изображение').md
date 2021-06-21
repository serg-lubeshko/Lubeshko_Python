# ИЗОБРАЖЕНИЯ models.ImageField(verbose_name='Изображение')

В setting.py необходимо указать маршрут к статитике и медиа

**STATICFILES_DIRS**  - дериктории, где  Джанго будет искать статические файлы, чтобы переместить в папку static 

```python
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'lsrproject/static'),
]

#emblem просто указал вместо media 
MEDIA_ROOT = os.path.join(BASE_DIR, 'emblem')
MEDIA_URL = '/emblem/'
```

Также в urls.py пропишем функцию static

```python
....
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
#MEDIA_URL -  константа, которую мы создали в settings.py
```

