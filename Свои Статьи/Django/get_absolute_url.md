# get_absolute_url (обратное разрешение адресов)

Сформировать интернет-адрес модели можно двумя способами: 

- *декларативным* - способ заключается в описании формата интернет-адреса в настройках проекта. Набор таких адресов оформляется в виде словаря Python и записывается в параметре `absolute_url_overrides` модуля settings.ру пакета конфигурации.
  Ключи элементов этого словаря должны иметь вид `<псевдоним приложения:>. <имя класса модели>.`  

  Пример объявления словаря, который на основе рубрики (экземпляра класса модели Rubric) сформирует адрес вида `bboard/<ключ рубрики>/`  , ведущий на страницу со списком объявлений, относящихся к этой рубрике:

  ```python
  ABSOLUTE_URL_OVERRIDES = {
  'bboard.rubric': lambda rec: "/bboard/%s/" % rec.pk,
  }
  <а href="{{ rubric.get_absolute_url }}">{{ rubric.name }}</a>
  
  ```

   

- *императивным* - способ заключается в непосредственном переопределении метода `get_absolute_url (self)` в классе модели.  Название метода определено по соглашению + Django использует это название в своих функциях.

  ```python
  exampl 1:
  class Rubric(models.Model):
      ....
  	def get_absolute_url(self):
  	return ”/bboard/%s/" % self.pk #такой подход не самый лучший для создания подобных методов. Лучше использовать функцию reverse()
  
  exampl 2:
      """path('detail/<int:room_id>/', DetailRooms, name="detail") -  строим маршрут. Строка из urls.py"""")
     ....
      def get_absolute_url(self):
          return reverse('detail', kwargs={"room_id":self.pk})
      """"
      detail - в url имя маршрута
      kwargs={"room_id":self.pk} - room_id параметр во view и <int:room_id>/  """
  
  ```

  При использовании метода `get_absolute_url  в return используем функцию ``reverse or reverse lazy`.  **reverse lazy** "больше строит маршрутов" чем `reverse`. 

  Затем в html, можем прописать

  ```html
  <a href={{ room.get_absolute_url }} class="card-link">Описание</a>
  room - экземпляр модели. взят из цикла {% for room in rooms %} ...{%endfor%}
  ```

  

