# on_delete. Параметр удаления объекта в модели

https://metanit.com/python/django/5.6.php

`on_delete` задает опцию удаления объекта текущей модели при удалении связанного объекта главной модели. Всего для параметра on_delete мы можем использовать следующие значения:

- **models.CASCADE**: автоматически удаляет строку из зависимой таблицы, если удаляется связанная строка из главной таблицы
- **models.PROTECT**: блокирует удаление строки из главной таблицы, если с ней связаны какие-либо строки из зависимой таблицы
- **models.SET_NULL**: устанавливает NULL при удалении связанной строка из главной таблицы
- **models.SET_DEFAULT**: устанавливает значение по умолчанию для внешнео ключа в зависимой таблице. В этом случае для этого столбца должно быть задано значение по умолчанию
- **models.DO_NOTHING**: при удалении связанной строки из главной таблицы не производится никаких действий в зависимой таблице

