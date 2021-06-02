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

<h4>Написать скрипты для следующего анализа:
1) Определить количество заявок в каждом месяце.

- <code>SELECT date_part('year', date_created) AS год, <br>
        date_part('month', date_created) AS месяц, <br>
        COUNT(*) AS "Кол-во заявок" <br>
        FROM credit_app_application <br>
        GROUP BY год, месяц <br>
        ORDER BY год, месяц DESC;</code>
  

2) Определить последнюю заявку по клиенту.

- <code>BLAH BLAH</code>
  

3) Определить клиентов, по которым были заведены заявки на другой продукт после одобрения.
   
- <code>BLAH BLAH</code></h4>

<h6>Все запросы написны для обращения к БД PostgreSQL.</h6>

<p></p>