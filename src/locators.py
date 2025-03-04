from selenium.webdriver.common.by import By


class BurgerLocators:
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, './/p[text()="Личный Кабинет"]')  # Кнопка "Личный кабинет" в навигации сайта
    CONSTRUCTOR_BUTTON = (By.XPATH, './/p[text()="Конструктор"]')  # Кнопка "Конструктор" в навигации сайта
    LOGO_BUTTON = (By.XPATH, './/*[contains(@class, "AppHeader_header__logo__2D0X2")]')  # Кнопка логотипа в навигации сайта
    GET_INTO_ACCOUNT_BUTTON = (By.XPATH, './/button[text()="Войти в аккаунт"]')   # Кнопка "Войти в аккаунт"
    CONSTRUCTOR_TITLE_BUTTON = (By.XPATH, './/*[text()="Соберите бургер"]')   # Заголовок конструктора "Соберите бургер"
    FORM_LOGIN_BUTTON = (By.XPATH, './/button[text()="Войти"]') # Кнопка "Войти в форме регистрации"
    FORM_LOGIN_LINK = (By.XPATH, './/a[text()="Войти"]') # Ссылка "Войти" в форме регистрации"
    FORM_REGISTRATION_BUTTON = (By.XPATH, './/button[text()="Зарегистрироваться"]')  # Кнопка "Зарегистрироваться" в форме регистрации
    FORM_INCORRECT_PASSWORD = (By.XPATH, './/p[text()="Некорректный пароль"]')   # Ошибка пароля в форме регистрации
    FORM_NAME_INPUT = (By.XPATH, './/label[text()="Имя"]/following-sibling::input')  # Поле ввода имени в форме регистрации
    FORM_EMAIL_INPUT = (By.XPATH, './/label[text()="Email"]/following-sibling::input') # Поле ввода почты в форме регистрации
    FORM_PASSWORD_INPUT = (By.XPATH, './/label[text()="Пароль"]/following-sibling::input') # Поле ввода пароля в форме регистрации
    MAKE_ORDER_BUTTON = (By.XPATH, './/button[text()="Оформить заказ"]') # Кнопка "Оформить заказ"
    LOGOUT_BUTTON = (By.XPATH, './/button[text()="Выход"]')  # Кнопка "Выход" из профиля
    # "Булки", "Соусы", "Начинки"
    BREADS_NO_SELECT = (By.XPATH, './/span[text()="Булки"]')
    TOPPING_NO_SELECT = (By.XPATH, './/span[text()="Начинки"]')
    SAUCES_NO_SELECT = (By.XPATH, './/span[text()="Соусы"]')
    # "Булки", "Соусы", "Начинки" ВЫБРАНЫ
    BREADS_SELECT = (By.XPATH, ".//div[contains(@class, 'tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect')" "and span/text()='Булки']")
    TOPPING_SELECT = (By.XPATH, ".//div[contains(@class, 'tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect')" "and span/text()='Начинки']")
    SAUCES_SELECT = (By.XPATH,  ".//div[contains(@class, 'tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect')" "and span/text()='Соусы']")

