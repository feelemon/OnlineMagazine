Описание проекта SoundFilch
========================================


Общие сведения
--------------

**Music Store**, **TAG: #Music, #Free, #Download, #Roscomzazor**

### Описание проекта:
-------------------------------------------------------

[Wiki](http://wiki.cs.hse.ru/Проектная_работа_2_курс_(2016)) [Github](https://github.com/feelemon/OnlineMagazine) [Внешняя сторона проекта](https://drive.google.com/file/d/0B3fs3UtoJ8aZYW4tVnJrcEFHcnc/view?usp=sharing) [Функционал] (
https://drive.google.com/file/d/0B3fs3UtoJ8aZVFJUVDI2dGZhZEk/view?usp=sharing) [ER-Diagram] (https://drive.google.com/file/d/0B3fs3UtoJ8aZdEpiYm8xVkZ2LTg/view?usp=sharing)

SoundFilch - онлайн магазин по продаже музыки, оснащенный функцией прослушивания перед покупкой (preview) и определяющий права исполнителя по сигнатуре дорожки со смежного сервиса.

Сервис состоит из: витрины/каталога товаров, разбитых по категориям; корзины, в которую пользователь может добавлять покупки; для электронных товаров реализована возможность скачать (или получить по почте) и оплата с помощью PayPal (наиболее простой для интеграции, для проекта достаточно показать работу с разработческим апи PayPal) или другими системами оплаты. Для неэлектронных товаров должна быть возможность указать их наличие, при покупке количество изменяется. В магазине могут быть промоакции: скидка при оформлении заказа по промокоду, скидка при заказе на определенную сумму, временная скидка на конкретную категорию товаров.

Постановка задачи
-----------------
Что необходимо реализовать:

* Витрина магазина с категориями
* Корзина пользователя, в которую можно добавлять или удалять товары.
* После оформления заказа, письмо с данными о заказе и пользователе отправляется на почту владельца магазина
* Приложение защищено от инъекций к базе
* Приложение работает с неэлектронными товарами, меняется количество доступного товара.
* Приложение защищено от XSS-атак.
* В приложении есть возможность оплатить с помощью сервисов онлайн-платежей.
* Сервис готов к запуску (по чеклисту выполнено все или почти все)

Используемые инструменты при проектировании
-----------------------------------------
* draw.io - инструмент для рисования схем и прототипа интерфейса
* ninjamock.com - сервис для прототипирования интерфейса
* Django - программный каркас для веб-приложений на языке Python.
* Bootstrap - фреймворк для разработки адаптивных и мобильных web-проектов.
* MySQL - система управления базами данных

Основные возомжности:
 * Послушать песню
 * Получить подробные сведения об исполнителе и композиции
 * Скачать с пиратского сайта по предоставленной ссылке
 * Отблагодарить разработчика
 * Посмотреть список прослушанных и скаченных
 * Рассказать друзьям
 * Комментировать
