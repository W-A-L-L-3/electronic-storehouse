# Электронный склад

Московская предпрофессиональная олимпиада школьников.

Профиль "Информационные технологии".

Командный кейс №5 "Электронный склад"

[Исходный текст технического задания](https://github.com/W-A-L-L-3/electronic-storehouse/blob/main/docs/technical-requirements.pdf)

## Кратное описание

Информационный сервис обеспечивающий взаимодействие пользователей (операторов) с автоматизированным складом.

## Функциональность

1. Добавление нескольких позиций из поставки на склад.
2. Отображение в виде списка позиций (товаров), с указанием ячейки, в которой товар находится на складе (по запросу в
   пользовательском интерфейсе).

3. Выбор определенного товара (позиции), для осуществления выдачи его аппаратной частью.
4. Наличие удалённого склада для позиций, которые невозможно разместить на основном складе.
5. Отображение в виде списка позиций (товаров), находящихся на удалённом складе.

## Интерфейс приложения

### Главное окно

#### До инициализации склада

![main_window_1](https://github.com/W-A-L-L-3/electronic-storehouse/blob/main/docs/img/main_window_1.jpg)

**1** - Инициализация склада.

При успешной инициализации появится всплывающие уведомление:

![successful_initialization](https://github.com/W-A-L-L-3/electronic-storehouse/blob/main/docs/img/successful%20initialization.jpg)

Если произошла ошибка во время связи с API для инициализации:

![receiving_error](https://github.com/W-A-L-L-3/electronic-storehouse/blob/main/docs/img/receiving_error.jpg)

#### После инициализации склада

![main_window_2](https://github.com/W-A-L-L-3/electronic-storehouse/blob/main/docs/img/main_window_2.jpg)

**2** - Добавление нескольких позиций из поставки на склад.

**3** - Отображение в виде списка позиций (товаров), с указанием ячейки, в которой товар находится на складе.

**4** - Выбор определенного товара (позиции), для осуществления выдачи его аппаратной частью.

**5** - Отображение в виде списка позиций (товаров), находящихся на удалённом складе.

____

### Окно для добавления товаров на склад

![adding_window_1](https://github.com/W-A-L-L-3/electronic-storehouse/blob/main/docs/img/adding_window_1.jpg)

**1** - Добавить строчку для ещё одного товара.

**2** - Отправить товары на склад.

После двух нажатий кнопки **1**:

![adding_window_2](https://github.com/W-A-L-L-3/electronic-storehouse/blob/main/docs/img/adding_window_2.jpg)

Корректный ввод позиций:

![adding_window_3](https://github.com/W-A-L-L-3/electronic-storehouse/blob/main/docs/img/adding_window_3.jpg)

Некорректный ввод позиций:

![adding_window_4](https://github.com/W-A-L-L-3/electronic-storehouse/blob/main/docs/img/adding_window_4.jpg)

При успешной отправке товаров на склад появится всплывающие уведомление:

![correct_adding](https://github.com/W-A-L-L-3/electronic-storehouse/blob/main/docs/img/correct_adding.jpg)

Если значение в каком-либо из полей в поставке некорректно:

![value_error](https://github.com/W-A-L-L-3/electronic-storehouse/blob/main/docs/img/value_error.jpg)

____

### Окно для отображения позиций (товаров), находящихся на складе

![info_window](https://github.com/W-A-L-L-3/electronic-storehouse/blob/main/docs/img/info_window.jpg)

____

### Окно для выбора определенного товара (позиции), для осуществления выдачи его аппаратной частью.

![taking_window](https://github.com/W-A-L-L-3/electronic-storehouse/blob/main/docs/img/taking_window.jpg)

При успешном выборе и выдаче товара появится всплывающие уведомление:

![correct_taking](https://github.com/W-A-L-L-3/electronic-storehouse/blob/main/docs/img/correct_taking.jpg)

Если товара с введённым названием нет на складе:

![taking_error](https://github.com/W-A-L-L-3/electronic-storehouse/blob/main/docs/img/taking_error.jpg)

____

### Окно для отображения позиций (товаров), находящихся на удалённом складе

![remote_info_window](https://github.com/W-A-L-L-3/electronic-storehouse/blob/main/docs/img/remote_info_window.jpg)
