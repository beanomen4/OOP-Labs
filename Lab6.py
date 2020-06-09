class Function():
    @staticmethod
    def findprice(coffee_grinding_stage, typepackaging, money1, money2, money3, money4, money5, money6):
        price = 100
        if typepackaging == "Coffee in Can":
            if coffee_grinding_stage == "Beans Coffee":
                price = money1
            if coffee_grinding_stage == "Ground Coffee":
                price = money2
            if coffee_grinding_stage == "Instant Coffee":
                price = money3
        if typepackaging == "Coffee in Bags":
            if coffee_grinding_stage == "Beans Coffee":
                price = money4
            if coffee_grinding_stage == "Ground Coffee":
                price = money5
            if coffee_grinding_stage == "Instant Coffee":
                price = money6
        return price


class Van:
    def __init__(self):
        self.max_kg = 100  # В кг и упаковках
        self.speendmoney = 0
        self.NameandQuality = dict()

    def load_up_the_Van(self, A):
        self.speendmoney += A.price
        self.max_kg -= A.quantity
        self.NameandQuality.update({int(A.pricenakg): str(A.name) + " (" + str(A.coffee_grinding_stage + ")")})

    def run_Van(self):
        # Заданый диапазон
        minvalue, maxvalue = 10, 500
        print("Free space - " + str(self.max_kg) + " kg ")
        print("Speend money - " + str(self.speendmoney) + " griven")
        for i in self.NameandQuality:
            print(str(i) + " cost/kg is " + self.NameandQuality[i])
        for i in range(minvalue, maxvalue):
            for k in self.NameandQuality:
                if i == int(k):
                    print("Product " + self.NameandQuality[k] + " in this range (" + str(minvalue) +","+str(maxvalue)+")")

###############Кофе и его Виды##########################
class Coffee:
    # Пример Вид=Арабика, Сорт кофе=Арабика Желтый бурбон, typepackaging=в банках, количестов=30 (упаковок 1 кг), Цена=30*200=6000 (за все,
    # учитовая тип упаковки)
    def __init__(self, quantity, coffee_grinding_stage, typepackaging):
        pass


###############Сорты и их цена##########################

#############Сорты Арабики###########################
class Arabica_Yellow_Bourbon(Coffee):
    def __init__(self, quantity, coffee_grinding_stage, typepackaging):
        super().__init__(quantity, coffee_grinding_stage, typepackaging)
        self.quantity = quantity
        self.pricenakg = Function.findprice(coffee_grinding_stage, typepackaging, 370, 400, 430, 420, 450, 470)
        self.coffee_grinding_stage = coffee_grinding_stage
        self.price = self.pricenakg * self.quantity
        self.name = "Arabica Yellow Bourbon"


class Arabica_Jamaica_Blue_Mountain(Coffee):
    def __init__(self, quantity, coffee_grinding_stage, typepackaging):
        super().__init__(quantity, coffee_grinding_stage, typepackaging)
        self.quantity = quantity
        self.pricenakg = Function.findprice(coffee_grinding_stage, typepackaging, 3500, 3650, 3965, 3555, 3555, 4010)
        self.coffee_grinding_stage = coffee_grinding_stage
        self.price = self.pricenakg * self.quantity
        self.name = "Arabica Jamaica Blue Mountain"


class Arabica_Nepal_Everest_Organic(Coffee):
    def __init__(self, quantity, coffee_grinding_stage, typepackaging):
        super().__init__(quantity, coffee_grinding_stage, typepackaging)
        self.quantity = quantity
        self.pricenakg = Function.findprice(coffee_grinding_stage, typepackaging, 1465, 1580, 1780, 1505, 1530, 1740)
        self.price = self.pricenakg * self.quantity
        self.coffee_grinding_stage = coffee_grinding_stage
        self.name = "Arabica Nepal Everest Organic"


class Arabica_Zambia_Lupeli(Coffee):
    def __init__(self, quantity, coffee_grinding_stage, typepackaging):
        super().__init__(quantity, coffee_grinding_stage, typepackaging)
        self.quantity = quantity
        self.pricenakg = Function.findprice(coffee_grinding_stage, typepackaging, 400, 420, 450, 435, 466, 500)
        self.price = self.pricenakg * self.quantity
        self.coffee_grinding_stage = coffee_grinding_stage
        self.name = "Arabica Zambia Lupeli"


class Arabica_Bali(Coffee):
    def __init__(self, quantity, coffee_grinding_stage, typepackaging):
        super().__init__(quantity, coffee_grinding_stage, typepackaging)
        self.quantity = quantity
        self.pricenakg = Function.findprice(coffee_grinding_stage, typepackaging, 360, 420, 450, 400, 455, 460)
        self.price = self.pricenakg * self.quantity
        self.coffee_grinding_stage = coffee_grinding_stage
        self.name = "Arabica Bali"


class Arabica_Sumatra(Coffee):
    def __init__(self, quantity, coffee_grinding_stage, typepackaging):
        super().__init__(quantity, coffee_grinding_stage, typepackaging)
        self.quantity = quantity
        self.pricenakg = Function.findprice(coffee_grinding_stage, typepackaging, 670, 720, 770, 705, 760, 770)
        self.price = self.pricenakg * self.quantity
        self.coffee_grinding_stage = coffee_grinding_stage
        self.name = "Arabica Sumatra"


###############Сорты Робусты####################################
class Java_Ineak(Coffee):
    def __init__(self, quantity, coffee_grinding_stage, typepackaging):
        super().__init__(quantity, coffee_grinding_stage, typepackaging)
        self.quantity = quantity
        self.pricenakg = Function.findprice(coffee_grinding_stage, typepackaging, 1000, 1120, 1320, 1100, 1300, 1380)
        self.price = self.pricenakg * self.quantity
        self.coffee_grinding_stage = coffee_grinding_stage
        self.name = "Java Ineak"


class Nany(Coffee):
    def __init__(self, quantity, coffee_grinding_stage, typepackaging):
        super().__init__(quantity, coffee_grinding_stage, typepackaging)
        self.quantity = quantity
        self.pricenakg = Function.findprice(coffee_grinding_stage, typepackaging, 2200, 2320, 2400, 2220, 2340, 2440)
        self.coffee_grinding_stage = coffee_grinding_stage
        self.price = self.pricenakg * self.quantity
        self.name = "Nany"


##################    MAIN    ############################################
class Main:
    print(9215 % 13)

    FURA = Van()

    A = Arabica_Yellow_Bourbon(30.5, "Beans Coffee", "Coffee in Bags")
    B = Arabica_Zambia_Lupeli(50.5, "Beans Coffee", "Coffee in Bags")
    C = Arabica_Sumatra(5, "Ground Coffee", "Coffee in Can")
    D = Java_Ineak(6, "Instant Coffee", "Coffee in Can")

    FURA.load_up_the_Van(A)
    FURA.load_up_the_Van(B)
    FURA.load_up_the_Van(C)
    FURA.load_up_the_Van(D)

    FURA.run_Van()
# Для переменной coffee_grinding_stage - "Beans Coffee", "Ground Coffee", "Instant Coffee"
# Для переменной typepackaging - "Coffee in Can", "Coffee in Bags"
# quantity = int, Количество упаковок
