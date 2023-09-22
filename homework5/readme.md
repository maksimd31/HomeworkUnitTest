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

*Задание 2. *Ниже список тестовых сценариев. Ваша задача - определить тип каждого теста (юнит-тест, интеграционный тест, сквозной тест) и объяснить, почему вы так решили.
Проверка того, что функция addContact корректно добавляет новый контакт в список контактов"".
""Проверка того, что при добавлении контакта через пользовательский интерфейс, контакт корректно отображается в списке контактов"".
""Проверка полного цикла работы с контактом: создание контакта, его редактирование и последующее удаление"".

*Формат сдачи: *подписанный google docs с правами на редактирование.