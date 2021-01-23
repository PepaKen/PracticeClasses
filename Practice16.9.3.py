class User:
    def __init__(self, firstname, lastname, balance):
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance

    def getInfo(self):
        return f'Клиент "{self.firstname} {self.lastname}". Баланс: {self.balance} руб.'


user_1 = User("Иван", "Петров", 50)

print(user_1.getInfo())
