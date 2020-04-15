# Диплом "Генератор учебного расписания"

## Описание:

- Автор: Ткаченко Никита Андреевич, 10Б
- Научный руководитель: Наумов Алексей Леонидович
- Год реализации: 2019-2020
- Язык реализации: Python 3.8.1

Данные диплом посвящен проблеме *генерации оптимального расписания*. Нередко составить качественное расписание для нескольких классов, которые подходят под заданные условия бывает трудоемко и неэффективно. **Главная цель данного диплома** - попробовать применить генетический алгоритм к данной задаче.

## Продукт:


Продуктом данной работы является программа, которая, используя генетический алгоритм, по заданным параметрам *(количество уроков, набор уроков, дни недели, ..)* создает приближенное к идеальному расписание. Расписания сохраняются в формате CSV и удовлетворяют поставленным условиям *(к примеру, недопустимо 3 одинаковых урока подряд, или недопустимо одни и те же уроки у разных классов в одно и то же время)* и параметрам.

- Примеры файлов с параметрами и выходных файлов находятся в папке *examples*.

#### Теория:


Задача по нахождению оптимального рещения, или дисциплина "Исследование операций" существует уже давно. Во время Второй мировой войны эта дисциплина широко применялась для планирования боевых действий, противолодочных рейдов, после - для реорганизации производства, составления планов снабжения, продажи сезонных товаров, составления расписания и многих других. Сама наука тесно связана с системным анализом, математическим программированием, методами искусственного интелекта и другими направлениями, включающие в себя эвристические методы. Генетический алгоритм относится к одним из таких методов.

**Генетический алгоритм** - эвристический алгоритм поиска (ответ может быть не идеально точным, но достаточно точным для поставленной задачи), который решает задачи с использованием механизма, похожего на естественный отбор в природе.

**Основные понятия:**
- Днк - набор параметров, который описывает, как выглядит и ведет себя объект (в данном случае - расписание)
- Ген - параметр, который описывает один признак объекта (к примеру, один урок) 
- Популяция - набор объектов, каждый со своим днк.
- Приспособленность (fitness) - значение, которое определяет, насколько хорошо данное днк подходит к поставленной задаче (насколько близок объект к идеальному)
- Скрещивание - процесс, во время которого из двух различных объектов создается 1 "ребенок".
- Мутация - процесс, благодаря которому в Днк может случайно измениться один из параметров в лучшую или худшую сторону.
- Селекция - отбор лучших объектов в новоую популяцию.


**Главная структура алгоритма выглядит так:**
- Задать идеал, к которому стремится алгоритм
- Создать начальную популяцию днк
- Цикл:
  1. Скрещивание
  2. Мутация
  3. Вычисление значения Приспособленности для каждого объекта
  4. Селекция
  
Цикл продолжается до тех пор пока не будет получен достаточно близкий к идеалу объект, либо количество популяций достигнет установленного граничения

#### Структура программы:

**Основные определения:** 
- Расписание - план школьных уроков за определенный промежуток времени (день, неделя, месяц, ...)
- Урок - промежуток времени, во время которого ученики изучают 1 определенный предмет (математика, русск)
- Генератор - [Фабрика](https://ru.wikipedia.org/wiki/%D0%A4%D0%B0%D0%B1%D1%80%D0%B8%D1%87%D0%BD%D1%8B%D0%B9_%D0%BC%D0%B5%D1%82%D0%BE%D0%B4_(%D1%88%D0%B0%D0%B1%D0%BB%D0%BE%D0%BD_%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F\) "Фабрика") [класса](https://ru.wikipedia.org/wiki/%D0%9A%D0%BB%D0%B0%D1%81%D1%81_(%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5\) "класс").

**Список файлов и классов:**
- main - основной файл программы. Здесь программа получает параметры из конфигурационного файла,
создает все необходимые объекты и вызывает нужные функции для работы генератора. 
- model - файл со всеми моделями
  1. WeeklySchedule - расписание на неделю.
  2. DailyClassSchedule - расписание на один день для одного класса.
  3. ScheduledLesson - запланированный урок.
- generators - файл в котором хранятся все генераторы. 
  1. WeeklyScheduleGenerator - Генератор расписания на неделю.
- fitness_calculator - файл, в котором вычисляется значение приспособления для расписания.
  1. WeeklyScheduleFitnessCalculator - класс вычисления значения приспособления для одного расписания.
- crossover - файл скрещивания расписанийю
  1. WeeklyScheduleCrossover - класс по скрещиванию одной популяции.
- serializer - файл по сериализации и выводу расписания.
  1. Serializer - класс, который выводит расписание в текстовый файл.
  2. Csv_serializer - класс, который выводит расписание в файл формата .csv (для просмотра с помощью электронных таблиц)
- optimizer - файл, в котором производится поиск оптимального расписания.
  1. GenericOptimizer - главный класс программы. В нем производятся все нужные операции для нахождения наиболее схожее с идеальным расписание.
- Общие классы:
  1. Factory - Фабрика определенного класса.
  2. ConfigurationClass - класс, в который передаются параметры для успешной работы другого класса.
  
## Инструкция по использованию и установке:
`Note: Для нормальной установки и работы программы требуется Python версии 3+ и установленный Pip.`
1. Скачать архив с программой из GitHub 

![Кнопка загрузки](/static/Pictures/dd_btn.png "Кнопка загрузки")

2. Открыть командную строку (`win+r`) и перейти в папку программы (с помощью команды `cd путь`)
3. Установить необходимые библиотеки с помощью команды `pip install -r requirements.txt`
4. Запустить файл main.py: `python main.py` 

Примеры файлов находятся в папке `examples`, конфигурационный файл называется `config.yaml`, выходные файлы находятся в папке `outputs`. 
 
