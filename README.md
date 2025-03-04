# UI автотесты для сервиса [Stellar Burgers](https://stellarburgers.nomoreparties.site/)
___
## Структура проекта:

`src`
- `config.py`   _Содержатся различные URL_
- `locators.py` _Локаторы элементов страниц_
- `data.py` _Тестовые данные пользователя_

`tests`
- `test_user_registration.py` _регистрация_
- `test_user_login.py` _вход в профиль_
- `test_user_logout.py` _выход из профиля_
- `test_to_constructor_navigation.py` _переход по клику на "Конструктор" и на логотип "Stellar Burgers."_
- `test_to_personal_account_navigation.py` _переход в личный кабинет_
- `test_to_sections_constructor_navigation.py` _переход по разделам "булки", "соусы" и "начинки"_

`constest.py` _Фикстуры проекта_  
`requirements.txt` _Зависимости проекта_

---
## Установите проект

    Клонируйте репозиторий
    Установите зависимости: pip install -r requirements.txt

## Запустите тесты
    Убедитесь, что у вас установлен Google Chrome

---
## Тесты
`test_user_registration.py` 
- `test_registration` _валидная регистрация_
- `test_incorrect_registration` _невалидная регистрация_

`test_user_login.py` 
- `test_login_into_account` _кликаем на "Войти в аккаунт"_
- `test_login_personal_account`  _кликаем на "Личный кабинет"_
- `test_login_form` _на странице регистр. кликаем на "войти"_
- `test_login_forgot` _на странице восстановления пароля кликаем на "войти"_

`test_user_logout.py`
- `test_user_logout` _логинимся, входим в "Личный кабинет" и выходим из него_


`test_to_personal_account_navigation.py`
- `test_personal_account_nav` _тест навигации в "Личный кабинет"_

`test_to_constructor_navigation.py`
- `test_to_constructor_navigation` _логинимся, переходим в личный кабинет, затем кликаем на "конструктор"_
- `test_to_logo_navigation` _логинимся, переходим в личный кабинет, затем кликаем на логотип_

`test_to_sections_constructor_navigation.py` 
- `test_section_breads` _сначала кликаем по секции "соусы", затем кликаем на "булки"_
- `test_section_sauces`_кликаем на секцию "соусы"_
- `test_section_toppings`_кликаем на секцию "начинки"_



