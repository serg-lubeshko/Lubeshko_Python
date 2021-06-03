But I wanted to point out that the opinion expressed in the [accepted answer](https://stackoverflow.com/a/1737078/6451573) is somewhat outdated. According to more recent discussions (django bugs [#7634](https://code.djangoproject.com/ticket/7634) and [#12785](https://code.djangoproject.com/ticket/12785)), auto_now and auto_now_add are not going anywhere, and even if you go to the [original discussion](http://groups.google.com/group/django-developers/browse_thread/thread/4cd631c225cb4e52), you'll find strong arguments against the RY (as in DRY) in custom save methods.

A better solution has been offered (custom field types), but didn't gain enough momentum to make it into django. You can write your own in three lines (it's [Jacob Kaplan-Moss' suggestion](https://groups.google.com/forum/#!msg/django-developers/TNYxwiXLTlI/L7srKCO8eEsJ)).

```python
from django.db import models
from django.utils import timezone


class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()

#usage
created_at = models.DateField(default=timezone.now)
updated_at = AutoDateTimeField(default=timezone.now)
```

