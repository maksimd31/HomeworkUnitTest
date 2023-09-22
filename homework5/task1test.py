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
