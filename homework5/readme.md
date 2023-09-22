Unit-тесты (семинары)
Урок 5. Другие виды тестирования
*Задание 1. *Представьте, что вы работаете над разработкой простого приложения для записной книжки, которое позволяет пользователям добавлять, редактировать и удалять контакты. 
Ваша задача - придумать как можно больше различных тестов (юнит-тесты, интеграционные тесты, сквозные тесты) для этого приложения. Напишите название каждого теста, его тип и краткое описание того, что этот тест проверяет.

Решение ниже 
1. Юнит-тесты:
   - `test_add_contact_success`: проверяет, что функция `add_contact` успешно добавляет новый контакт в список контактов.
   ```python
   def test_add_contact_success():
       contacts = []
       contact = Contact(name="John", phone="1234567890")
       add_contact(contacts, contact)
       assert len(contacts) == 1
   ```

   - `test_add_contact_duplicate`: проверяет, что функция `add_contact` корректно обрабатывает дубликаты контактов и не добавляет повторяющиеся контакты.
   ```python
   def test_add_contact_duplicate():
       contacts = [Contact(name="John", phone="1234567890")]
       contact = Contact(name="John", phone="1234567890")
       add_contact(contacts, contact)
       assert len(contacts) == 1
   ```

   - `test_edit_contact_success`: проверяет, что функция `edit_contact` правильно изменяет данные контакта.
   ```python
   def test_edit_contact_success():
       contacts = [Contact(name="John", phone="1234567890")]
       new_contact = Contact(name="John Doe", phone="9876543210")
       edit_contact(contacts, 0, new_contact)
       assert contacts[0].name == "John Doe"
   ```

   - `test_delete_contact_success`: проверяет, что функция `delete_contact` успешно удаляет контакт из списка контактов.
   ```python
   def test_delete_contact_success():
       contacts = [Contact(name="John", phone="1234567890")]
       delete_contact(contacts, 0)
       assert len(contacts) == 0
   ```

2. Интеграционные тесты:
   - `test_add_contact_ui_success`: проверяет, что при добавлении контакта через пользовательский интерфейс, контакт корректно добавляется в список контактов.
   ```python
   def test_add_contact_ui_success():
       app = App()
       app.open_add_contact_page()
       app.fill_contact_form(name="John", phone="1234567890")
       app.submit_contact_form()
       assert len(app.get_contacts()) == 1
   ```

   - `test_edit_contact_ui_success`: проверяет, что при редактировании контакта через пользовательский интерфейс, изменения сохраняются в списке контактов.
   ```python
   def test_edit_contact_ui_success():
       app = App()
       app.open_edit_contact_page(0)
       app.fill_contact_form(name="John Doe", phone="9876543210")
       app.submit_contact_form()
       assert app.get_contact(0).name == "John Doe"
   ```

   - `test_delete_contact_ui_success`: проверяет, что при удалении контакта через пользовательский интерфейс, контакт удаляется из списка контактов.
   ```python
   def test_delete_contact_ui_success():
       app = App()
       app.open_delete_contact_page(0)
       app.confirm_delete()
       assert len(app.get_contacts()) == 0
   ```

3. Сквозные тесты:
   - `test_full_contact_lifecycle`: проверяет полный цикл работы с контактом: создание контакта, его редактирование и последующее удаление.
   ```python
   def test_full_contact_lifecycle():
       app = App()

       # Создание контакта
       app.open_add_contact_page()
       app.fill_contact_form(name="John", phone="1234567890")
       app.submit_contact_form()

       # Редактирование контакта
       app.open_edit_contact_page(0)
       app.fill_contact_form(name="John Doe", phone="9876543210")
       app.submit_contact_form()

       # Удаление контакта
       app.open_delete_contact_page(0)
       app.confirm_delete()

       assert len(app.get_contacts()) == 0
   ```
Итого 
```python
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class App:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def edit_contact(self, index, contact):
        self.contacts[index] = contact

    def delete_contact(self, index):
        del self.contacts[index]

    def get_contacts(self):
        return self.contacts

    def open_add_contact_page(self):
        # Логика открытия страницы добавления контакта
        pass

    def fill_contact_form(self, name, phone):
        # Логика заполнения формы контакта
        pass

    def submit_contact_form(self):
        # Логика отправки формы контакта
        pass

    def get_contact(self, index):
        return self.contacts[index]

    def open_edit_contact_page(self, index):
        # Логика открытия страницы редактирования контакта
        pass

    def open_delete_contact_page(self, index):
        # Логика открытия страницы удаления контакта
        pass

    def confirm_delete(self):
        # Логика подтверждения удаления контакта
        pass


def test_add_contact_success():
    contacts = []
    contact = Contact(name="John", phone="1234567890")
    App.add_contact(contacts, contact)
    assert len(contacts) == 1


def test_add_contact_duplicate():
    contacts = [Contact(name="John", phone="1234567890")]
    contact = Contact(name="John", phone="1234567890")
    App.add_contact(contacts, contact)
    assert len(contacts) == 1


def test_edit_contact_success():
    contacts = [Contact(name="John", phone="1234567890")]
    new_contact = Contact(name="John Doe", phone="9876543210")
    App.edit_contact(contacts, 0, new_contact)
    assert contacts[0].name == "John Doe"


def test_delete_contact_success():
    contacts = [Contact(name="John", phone="1234567890")]
    App.delete_contact(contacts, 0)
    assert len(contacts) == 0


def test_add_contact_ui_success():
    app = App()
    app.open_add_contact_page()
    app.fill_contact_form(name="John", phone="1234567890")
    app.submit_contact_form()
    assert len(app.get_contacts()) == 1


def test_edit_contact_ui_success():
    app = App()
    app.open_edit_contact_page(0)
    app.fill_contact_form(name="John Doe", phone="9876543210")
    app.submit_contact_form()
    assert app.get_contact(0).name == "John Doe"


def test_delete_contact_ui_success():
    app = App()
    app.open_delete_contact_page(0)
    app.confirm_delete()
    assert len(app.get_contacts()) == 0


def test_full_contact_lifecycle():
    app = App()

    # Создание контакта
    app.open_add_contact_page()
    app.fill_contact_form(name="John", phone="1234567890")
    app.submit_contact_form()

    # Редактирование контакта
    app.open_edit_contact_page(0)
    app.fill_contact_form(name="John Doe", phone="9876543210")
    app.submit_contact_form()

    # Удаление контакта
    app.open_delete_contact_page(0)
    app.confirm_delete()

    assert len(app.get_contacts()) == 0


```


*Задание 2. *Ниже список тестовых сценариев. Ваша задача - определить тип каждого теста (юнит-тест, интеграционный тест, сквозной тест) и объяснить, почему вы так решили.
Проверка того, что функция addContact корректно добавляет новый контакт в список контактов"".
""Проверка того, что при добавлении контакта через пользовательский интерфейс, контакт корректно отображается в списке контактов"".
""Проверка полного цикла работы с контактом: создание контакта, его редактирование и последующее удаление"".

1. "Проверка того, что функция `addContact` корректно добавляет новый контакт в список контактов."
   - Тип теста: Юнит-тест.
   - Объяснение: Этот тест проверяет только логику и корректность работы функции `addContact`. Он не зависит от других компонентов системы и может быть выполнен независимо от них. Также, он фокусируется на одной специфичной функции, а не на целом взаимодействии между разными компонентами.

2. "Проверка того, что при добавлении контакта через пользовательский интерфейс, контакт корректно отображается в списке контактов."
   - Тип теста: Интеграционный тест.
   - Объяснение: Этот тест проверяет целостность и корректность работы между пользовательским интерфейсом и списком контактов. Он включает взаимодействие между разными компонентами, а именно пользовательским интерфейсом и функцией добавления контакта. Это помогает убедиться, что функциональность, связанная с отображением контакта в пользовательском интерфейсе, работает правильно.

3. "Проверка полного цикла работы с контактом: создание контакта, его редактирование и последующее удаление."
   - Тип теста: Сквозной тест.
   - Объяснение: Этот тест проверяет весь жизненный цикл контакта - создание, редактирование и удаление. Он охватывает несколько компонентов системы, таких как пользовательский интерфейс, функции создания, редактирования и удаления контакта, а также список контактов. Тест позволяет убедиться, что все компоненты работают правильно вместе и поддерживают ожидаемый функционал для полной работы с контактами.

Пример кода для данных тестов:

```python
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class App:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def edit_contact(self, index, new_contact):
        if 0 <= index < len(self.contacts):
            self.contacts[index] = new_contact

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            del self.contacts[index]

    def add_contact_ui(self, name, phone):
        # Логика взаимодействия с пользовательским интерфейсом
        # Например, получение введенных пользователем данных и передача их в функцию add_contact
        contact = Contact(name, phone)
        self.add_contact(contact)


# Юнит-тест
def test_add_contact_success():
    app = App()
    contact = Contact("John", "1234567890")
    app.add_contact(contact)
    assert len(app.contacts) == 1


# Интеграционный тест
def test_add_contact_ui_success():
    app = App()

    # Воспроизведение действий пользователя:
    app.add_contact_ui("John", "1234567890")

    assert len(app.contacts) == 1
    assert app.contacts[0].name == "John"


# Сквозной тест
def test_full_contact_lifecycle():
    app = App()

    # Создание контакта
    app.add_contact_ui("John", "1234567890")

    # Редактирование контакта
    app.edit_contact(0, Contact("John Doe", "9876543210"))

    assert app.contacts[0].name == "John Doe"

    # Удаление контакта
    app.delete_contact(0)

    assert len(app.contacts) == 0

```

*Формат сдачи: *подписанный google docs с правами на редактирование.