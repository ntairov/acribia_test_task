# Acribia Test Task 

### Необходимо реализовать Django-приложение следующим функционалом


С интерфейса на сервер приходит URL (валидация на client-side), например, вида:

- http://google.com

- https://google.com/

- https://www.google.com/maps/

- https://translate.google.ru/


Приложение должно проверять наличие диретктории на веб-сервере путём отправки HEAD запроса по URL, сформированному

конкатенацией исходного URL и директории из списка.

Запросы должны выполняться параллельно.

Результаты должны подгружаться на страницу динамически.


Список директорий можно взять отсюда:

https://raw.githubusercontent.com/puniaze/dirs3arch/master/db/dirbuster/directory-list-2.3-small.txt

Из этого списка необходимо предварительно удалить все строки, заканчивающиеся на ".%EXT%"

Ограничений по технологиям нет.

## Итоги :checkered_flag:

Ниже, я провел тесты асинхронных запросов, в качестве веб-сервера был взят всеми известный - http://youtube.com/

Было сделано 3 вида асинхронных запроса:

- Обычный асинхронный запрос
- Запрос с записью результатов в текстовый файл
- Запрос с записью в БД

### Обычный асинхронный запрос :running:

| № Request     |   seconds        |
| ------------- | -------------    |
| 1k requests   | ~ 1.3 - 1.78s    |
| 5k requests   | ~ 6.7 - 7.7s     |
| 10k requests  | ~ 12.4 - 13.2s   |

### Запрос с записью результатов в текстовый файл :runner:

| № Request     |   seconds     |
| ------------- | ------------- |
| 1k requests   | ~ 1.5 - 2.1s  |
| 5k requests   | ~ 7.3 - 7.8s  |
| 10k requests  |~ 13.3 - 16.1s |

Как мы видим, обычные запросы и запросы с записью в файл, почти не отличаются по времени выполнения.

P.S: Результаты двух таблиц, очень даже впечатляют :) :hourglass_flowing_sand:


### Запрос с записью результатов в БД :turtle:

| № Request     |  secs / mins    |
| ------------- | -------------   |
| 1k requests   | ~ 31 - 31.8s    |
| 5k requests   | ~ 2.60 - 2.96m  |
| 10k requests  | ~ 5.97 - 6.08m  |

### Были использованы следующие технологии :wrench:

 - [x] Python 3 / Django 2
 - [x] Aiohttp / Asyncio
 - [x] jQuery / Ajax

