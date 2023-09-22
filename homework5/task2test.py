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
