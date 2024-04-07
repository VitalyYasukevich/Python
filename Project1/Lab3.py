# # стол
# class Table:
#     __mass = 0
#
#     def __init__(self, mass0):
#         self.__mass = mass0
#
#     # чтение инкапсулированной массы
#     def get_mass(self):
#         return self.__mass
#
# #журнальный стол
# class JournalTable(Table):
#     storage = 0
#
#
# # обеденный стол
# class DinnerTable(Table):
#     __places = 0
#
#     def __init__(self, mass0):
#         Table.__init__(self, mass0)
#         self.__places = mass0//5
#
#     # чтение инкапсулированного числа мест
#     def get_places(self):
#         return self.__places
#
#
# class Truck:
#     __maxMass = 0
#     __tables = []
#
#     def __init__(self, max_mass):
#         self.__maxMass = max_mass
#
# #расчет всех погруженных столов
#     def __current_mass(self):
#         s = 0
#         for i in self.__tables:
#             s += i.get_mass()
#         return s
#
# #расчет оставшейся доступности массы для погрузки столов
#     def reserved_mass(self):
#         return self.__maxMass - self.__current_mass()
#
#     def add_table(self, new_table):
#         if new_table.get_mass() < self.reserved_mass():
#             self.__tables.append(new_table)
#             print("Стол массой  " +
#                   str(new_table.get_mass()) +
#                   " загружен!")
#         else:
#             print("Стол массой " +
#                   str(new_table.get_mass()) +
#                   " Не влазит!\nОсталось только " +
#                   str(self.reserved_mass()) + " кг!")
#
#
# newTable = [
#     DinnerTable(10),
#     DinnerTable(20),
#     DinnerTable(30)]
#
# newTruck = Truck(50)
# newTruck.add_table(newTable[0])
# newTruck.add_table(newTable[1])
# newTruck.add_table(newTable[2])

#----------------------------------------------------------------------------------------------------------------------
# Вариант 5
# Kласс Car: id, Марка, Модель, Год выпуска, Цвет, Цена, Регистрационный номер
# Функции-члены реализуют запись и считывание полей (проверка корректности), вывода возраста машины.
# Создать список объектов. Вывести:
# a) список автомобилей заданной марки;
# б) список автомобилей заданной модели, которые эксплуатируются больше n лет;
class Car:
    _id_autoincrement = 1

    def __init__(self, brand, model, yearOfIssue, color, price, registrationNumber):
        self.__id = Car._id_autoincrement        #id
        Car._id_autoincrement += 1
        self.__brand = brand                  # марка авто
        self.__model = model                  # модель авто
        self.__yearOfIssue = yearOfIssue      # год выпуска
        self.__color = color
        self.__price = price
        self.__registrationNumber = registrationNumber

    # Сеттер метод, изменяющий значение закрытого атрибута для экземпляра класса
    def set_id(self, id):
        self.__id = id

    def set_brand(self, brand):
        self.__brand = brand

    def set_model(self, model):
        self.__model = model

    def set_yearOfIssue(self, yearOfIssue):
        if yearOfIssue < 1924 or yearOfIssue > 2024:       # машине мах 100 лет
            print("Неверно введён год выпуска авто!!!")
        else:
            self.__yearOfIssue = yearOfIssue

    def set_color(self, color):
        self.__color = color

    def set_price(self, price):
        if price < 1 or price > 999999:
            raise ValueError("Неверно указана стоимость авто!!!")
        self.__price = price

    def set_registrationNumber(self, registrationNumber):
        self.__registrationNumber = registrationNumber

    # Геттер метод, возвращающий значение закрытого атрибута для экземпляра класса
    def get_id(self):
        return self.__id

    def get_brand(self):
        return self.__brand

    def get_model(self):
        return self.__model

    def get_yearOfIssue(self):
        return self.__yearOfIssue

    def get_color(self):
        return self.__color

    def get_price(self):
        return self.__price

    def get_registrationNumber(self):
        return self.__registrationNumber

    # метод вывода данных о машине
    @staticmethod
    def printCarInfo(car):
        print(f"ID: {car.__id}, "
            f"{car.__brand} "
            f"{car.__model}, "
            f"{car.__yearOfIssue} года, "
            f"Цвет: {car.__color}, "
            f"Стоимость: {car.__price}$, "
            f"Регистрационный номер: {car.__registrationNumber}")

    # метод вывода списка автомобилей заданной марки
    @classmethod
    def printCarBrand(cls, carList, brandCar):
        for i in range(len(carList)):
            if brandCar == carList[i].get_brand():
                print(carList[i])
            else:
                print("Автомобилей марки " + brandCar + " нет!")

    # метод вывода списка автомобилей заданной модели, которые эксплуатируются больше n лет
    @classmethod
    def printCarModel(cls, carList, modelCar, yearOfOperation):
        for i in range(len(carList)):
            if modelCar == carList[i].get_model() and yearOfOperation <= 2024 - yearOfOperation:
                print(carList[i])
            else:
                print("Автомобилей модели " + modelCar + " находящихся в эксплуатации " + yearOfOperation + " г. - нет!")


carList = []
count = int(input("Сколько машин будем вводить? "))

for i in range(count):
    brand = input("Введите марку: ")
    model = input("Введите модель: ")
    year = int(input("Введите год выпуска: "))
    color = input("Введите цвет: ")
    price = int(input("Введите стоимость: "))
    registrationNumber = input("Введите регистрационный номер: ")

    car = Car(brand, model, year, color, price, registrationNumber)
    carList.append(car)

# вывод данных авто на экран
for i in range(len(carList)):
    Car.printCarInfo(carList[i])

    # метод вывода возраста машины
    # @classmethod
    # def ageOfTheCar(cls, carList)



    print("\n*********************************************************************************************\n")
    # Вывод списка автомобилей заданной марки
    brandCar = input("Введите марку автомобиля для поиска: ")
    print(f"\nАвтомобили марки {brandCar}: ")
    Car.printCarBrand(carList, brandCar)

    print("\n*********************************************************************************************\n")
    # Вывод списка автомобилей заданной модели, которые эксплуатируются больше n лет
    modelCar = input("Введите модель автомобиля: ")
    yearOfOperation = input("Сколько годиков эскплуатируете? ")
    print(f"\nАвтомобили модели ({modelCar}), которые эксплуатировались более ({yearOfOperation}) лет.: ")
    Car.printCarModel(carList, modelCar, yearOfOperation)







        # car1 = Car(1, "Audi", "100", 2023, "Black", 45000, "3048-XK")
        # car2 = Car(2, "BMW", "525", 2022, "Brown", 43000, "0301-KE")
        # car3 = Car(3, "Mercedes-Benz", "S-class cabrio", 2021, "Red", 50000, "4639-HB")
        # car4 = Car(4, "Volvo", "S90", 2024, "Blue", 55000, "2506-LO")
        # car5 = Car(5, "Ford", "Explorer", 2021, "Silver", 35000, "5648-NY")

        # car5.set_price(345253)
        # print(car5.get_price())
        #
        # print(Car.car1)

