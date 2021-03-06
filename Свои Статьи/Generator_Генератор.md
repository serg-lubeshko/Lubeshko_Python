# Генератор Python

**Генератор** - это итератор, элементы которого можно перебирать (итерировать) один раз (генерирует значения по мере необходимости). Генератор поддерживает такие функции как `sum`, `max`, `min`

```python
Пример
b = (x**2 for x in range(10))
sum(b) #>>285

```

**Итератор** - это объект, который поддерживает функцию next() для перехода к следующему элементу коллекции.

**Итерируемый объект** - это объект, который позволяет поочередно обойти свои элементы и может быть преобразован к итератору (пример: список (a), для обхода используем for, но к итератору можем привести используя функцию foo = iter(a)) и обход осуществим используя функцию next(foo), *но только один раз*).

**Функция-генератор, или метод-генератор** – это функция, или метод, содержащая выражение yield. В результате обращения к функции-генератору возвращается итератор. Значения из итератора извлекаются по одному, с помощью его метода __next__(). При каждом вызове метода __next__() он возвращает результат вычисления выражения yield.  

**Выражения-генераторы**  -  синтаксически они очень похожи на генераторы списков, единственное отличие состоит в том, что они заключаются не в квадратные скобки, а в круглые.

```
Синтаксис:
(expression for item in iterable)
(expression for item in iterable if condition)
```

```python
def quarters(next_quarter=0.0):
    while True:
        received = (yield next_quarter)
        if received is None:
            next_quarter += 0.25
        else:
            next_quarter = received

result = []
generator = quarters()
while len(result) < 5:
    x = next(generator)
    if abs(x - 0.5) < sys.float_info.epsilon:
        x = generator.send(1.0)
    result.append(x)

print(result) >>>> [0.0, 0.25, 1.0, 1.25, 1.5]
```
## Генератор vs. функция

Дальше перечислены основные отличия между генератором и обычной функцией.

- Генератор использует `yield` для отправления значения пользователю, а у функции для этого есть `return`;
- При использовании генератора вызовов yield может быть больше чем один;
- Вызов yield останавливает исполнение и возвращает итератор, а return всегда выполняется последним;
- Вызов метода `next()` приводит к выполнению функции генератора;
- Локальные переменные и состояния сохраняются между последовательными вызовами метода `next()`;
- Каждый дополнительный вызов `next()` вызывает исключение `StopIteration`, если нет следующих элементов для обработки.

##### ПЛЮСЫ и МИНУСЫ ##

1. Экономия памяти
2. Обработка больших данных



