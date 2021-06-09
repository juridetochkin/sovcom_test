<h1> Тестовое задания для "Совком Банк" </h1>

<h2> Первая часть задания: </h2>

<h3>Техническое Задание:</h3>

<pre>
Реализовать Web приложение со следующим функционалом:
1. Отображение данных в виде таблицы
2. Возможность редактирования данных в этой таблице
3. Добавить валидаторы для ввода данных. Вводимые данные должны
соответствовать типу/маске поля.
4. При редактировании записи строка становится недоступной для
редактирования другими пользователями.
5. Возможность сортировки в таблице
6. Возможность поиска по таблице
7. Возможность выгрузки в Excel/csv данных из таблицы
8. Логирование изменений записей в таблице
Приоритет выполнения: 1, 2, 4, 8, 3, 5, 6, 7
Список полей:
1. Дата заявки
2. Продукт (возможные значения: Авто/Потреб/Залог/Ипотека)
3. Телефон клиента (должен соответствовать маске 0000000000)
4. Решение (возможные значения: Одобрено/Отказано/Временный отказ)
5. Комментарий к решению
Поля 1-3 обязательны для заполнения.
</pre>

<h3>Проверить приложение можно по адресу:</h3>
http://188.166.116.47:8000/ <br>

Использованные инструменты:
- Python 3.8
- Django 3.23
- django-filter, django-tables2, tablib
- uWSGI
- NGINX
- PostgreSQL 
- Ubuntu 20.04
<br><br>
  
Предзагруженные пользователи и пароли (для проверки):

1) - username: testadmin
    - password: 123456789To
    
2) - username: user1
    - password: 123456789To
    
3) - username: user2
    - password: 123456789To
    
Доступ к приложению разрешен только для зарегистрированных и авторизованных пользователей. <br>
Доступ к Логам приложения разрешен только Админам.

<h2> Вторая часть задания: </h2>

<h3>Написать скрипты для следующего анализа:</h3><br>

<h4>1) Определить количество заявок в каждом месяце.</h4>

<pre>
SELECT 
    date_part('year', date_created) AS "Год",
    date_part('month', date_created) AS "Месяц",
    COUNT(*) AS "Кол-во заявок"
FROM credit_app_application
GROUP BY "Год", "Месяц"
ORDER BY "Год", "Месяц" DESC;
</pre>


<h4>2) Определить последнюю заявку по клиенту.</h4>

- Для клиента с ID = 1 <br>

<pre>
SELECT *
FROM credit_app_application
WHERE client_id = 1
ORDER BY date_created DESC LIMIT 1
</pre>
  
- Или следующая комманда, если хотим получить ID последней заявки по каждому клиенту из БД: <br>
 
<pre>
SELECT 
    id AS "Номер Клиента",
    (
     SELECT id
     FROM credit_app_application AS P1
     WHERE P1.client_id = P.id
     ORDER BY date_created DESC LIMIT 1
     )
       AS " Номер последней заявки"
FROM credit_app_client AS P
GROUP BY id
ORDER BY id
</pre>
  

<h4>3) Определить клиентов, по которым были заведены заявки на другой продукт после одобрения.</h4>

<pre>
SELECT
    DISTINCT credit_app_application.client_id AS "Номер Клиента"
FROM 
    credit_app_application, 
    (
     SELECT *
     FROM credit_app_application
     WHERE decision = 'AP'
      ) 
        AS Approved
WHERE 
    credit_app_application.client_id = Approved.client_id 
    AND credit_app_application.date_created > Approved.date_created
    AND NOT credit_app_application.product = Approved.product
</pre>

<h5>Все запросы написаны для обращения к БД PostgreSQL.</h5>

<p></p>