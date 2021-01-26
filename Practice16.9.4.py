class Visitor:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname


class MoreInfo(Visitor):
    def __init__(self, firstname, lastname, place, status):
        super().__init__(firstname, lastname)
        self.place = place
        self.status = status

    def getInfo(self):
        return f"{self.firstname} {self.lastname}, {self.place}, статус: {self.status}"


visitor_1 = MoreInfo("Иван", "Петров", "г.Москва", "Наставник")
visitor_2 = MoreInfo("Василий", "Огарев", "г.Уфа", "Студент")
visitor_3 = MoreInfo("Аркадий", "Дубайло", "г.Москва", "Охранник")

print("Список гостей:",
      f"{visitor_1.getInfo()}",
      f"{visitor_2.getInfo()}",
      f"{visitor_3.getInfo()}", sep='\n')
