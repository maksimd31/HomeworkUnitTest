"""
Задание 3. (необязательное)
Добавьте функцию в класс UserRepository, которая разлогинивает всех пользователей, кроме
администраторов. Для этого, вам потребуется расширить класс User новым свойством, указывающим,
обладает ли пользователь админскими правами. Протестируйте данную функцию.
"""


class User:
    def __init__(self, username, is_admin=False):
        self.username = username
        self.is_admin = is_admin


class UserRepository:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def logout_non_admin_users(self):
        for user in self.users:
            if not user.is_admin:
                print(f"Logging out user: {user.username}")
                # Your logout logic here


if __name__ == "__main__":
    repository = UserRepository()
    repository.add_user(User("admin", True))
    repository.add_user(User("user1"))
    repository.add_user(User("user2"))
    repository.logout_non_admin_users()

# В данном примере мы создаем класс User, который имеет свойство is_admin,
# указывающее, является ли пользователь администратором. Затем класс UserRepository
# содержит функцию logout_non_admin_users, которая разлогинивает всех пользователей,
# кроме администраторов.
