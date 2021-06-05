<h1> Тестовое задания для "Совком Банк" </h1>

<h2> Первая часть задания: </h2>

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

- SELECT date_part('year', date_created) AS "Год", <br>
        date_part('month', date_created) AS "Месяц", <br>
  COUNT(*) AS "Кол-во заявок" <br>
  FROM credit_app_application <br>
  GROUP BY "Год", "Месяц" <br>
  ORDER BY "Год", "Месяц" DESC;
  

<h4>2) Определить последнюю заявку по клиенту.</h4>

-- Для клиента с ID = 1 <br>

- SELECT *<br>
  FROM credit_app_application<br>
  WHERE client_id = 1<br>
  ORDER BY date_created DESC LIMIT 1<br>
  
-- Или следующая комманда, если хотим получить ID последней заявки по каждому клиенту из БД: <br>
 
- SELECT id AS "Клиент",<br>
(<br>
  SELECT id <br>
  FROM credit_app_application AS P1 <br>
  WHERE P1.client_id = P.id <br>
  ORDER BY date_created DESC LIMIT 1<br>
  ) <br>
  AS " Номер последней заявки"<br>
FROM credit_app_client AS P<br>
GROUP BY id<br>
ORDER BY id<br>
  

<h4>3) Определить клиентов, по которым были заведены заявки на другой продукт после одобрения.</h4>
   
- <code>BLAH BLAH</code>

<h5>Все запросы написаны для обращения к БД PostgreSQL.</h5>

<p></p>