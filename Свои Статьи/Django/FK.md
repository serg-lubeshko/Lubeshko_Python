# FK

Связь ”один-со-многими” связывает одну запись первичной модели с произволь­ ным числом записей вторичной модели.

```python
ForeingKey(<связываемая первичная модель>,оп_delete=<поведение при удалении записи>[,<остальные параметры>])

```

##### **Первым**, позиционным, параметром указывается связываемая первичная модель в виде:

1. непосредственно ссылки на класс модели, если объявление первичной модели находится перед объявлением вторичной модели (БЕЗ кавычек)

2.  строки с именем класса, если первичная модель объявлена после вторичной:

   ```python
   class Bb(models.Model) :
   rubric = models.ForeignKey(’Rubric’, on_delete=models.PROTECT)
   class Rubric (models .Model) :
   ...
   ```

   

3. Ссылка на модель из другого приложения проекта записывается в виде строки формата `<имя приложения>.<имя класса модели>`:

   ```python
   rubric = models.ForeingKey('rubrics.Rubric’, on_delete=models.PROTECT)
   
   ```

4. Если нужно создать модель, ссылающуюся на себя (создать рекурсивную связь), то первым параметром конструктору следует передать строку self:

```python
parent_rubric = models. ForeingKey (’ self ’, on_delete=models. PROTECT)
```

##### Вторым [on_delete](см. on_delete)

##### Дополнительные необязательные параметры:

| FK параметры          | Описание                                                     | Пример                                                       |
| --------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| limit_choices_to = {} | позволяет вывести в раскрывающемся списке записей пер­вичной модели, отображаемом в веб-форме, только записи, удовлетворяющие заданным критериям фильтрации. | стр. 97 Дронов<br />rubric = models.ForeignKey(Rubric, on_delete=models.PROTECT, <br/>limit_choices_to={'show’: True}) |
| related_name=         | 1. имя атрибута записи первичной модели, предназначенного для доступа к связанным записям вторичной модели.<br /> 2.**Если доступ из записи первичной модели к связанным записям вторичной моде­ли не требуется,**достаточно присвоить пара­метру related_name СИМВОЛ "ПЛЮС"<br />3.Если параметр не указан, то атрибут такого рода получит стандартное имя вида <имя связанной вторичной модели>_set |                                                              |
| related_ name_query = | имя фильтра, которое будет применяться во вторичной модели для фильтрации по значениям из записи первичной модели: |                                                              |
| to_fieid              | имя поля первичной модели, по которому будет выполнена связь, <br/>в виде строки. Такое поле должно быть помечено как уникальное (параметр unique конструктора должен иметь значение True). |                                                              |
| db_constraint         | Если True, то в таблице базы данных будет создана связь, по­зволяющая сохранять ссылочную целостность; если False, ссылочная целостность будет поддерживаться только на уровне Django. |                                                              |


```python
#related_name
class Bb(models.Model) :
	rubric = models.ForeignKey(Rubric, on_delete=models.PROTECT, 
	related_name=’entries’)
# Получаем первую рубрику
first_rubric = Rubric.objects.first()
# Получаем доступ к связанным объявлениям через атрибут entries,
# указанный в параметре related_name
bbs = first_rubric.entries.all()

```

```python
#related_ name_query
class Bb(models.Model):
	rubric = models.ForeignKey(Rubric, on_delete=models.PROTECT, 
	related_query_name=’entry’)
# Получаем все рубрики, содержащие объявления о продаже домов,
# воспользовавшись фильтром, заданным в параметре related_query__name
rubrics = Rubric.objects.filter(entry__title='Дом')

```

