class TipisonColection:
    def __init__(self, Mashina):
        #Конструктор в який передається 1 об’єкт узагальненого класу
        self.TipisovaniObject = Mashina
        self.Interface = set()
    def __enter__(self):
        #Конструктор в який передається стандартна колекція об’єктів
        self.StandrtObj1 = Arabica_Yellow_Bourbon(5, "Beans Coffee", "Coffee in Bags")
        self.StandrtObj2 = Arabica_Jamaica_Blue_Mountain(6.5, "Beans Coffee", "Coffee in Bags")
    def __delete__(self, instance):
        #Пустой конструктор
        pass

class Coffee:
    def __init__(self, quantity, coffee_grinding_stage, typepackaging):
        pass

class Arabica_Yellow_Bourbon(Coffee):
    def __init__(self, quantity, coffee_grinding_stage, typepackaging):
        super().__init__(quantity, coffee_grinding_stage, typepackaging)
        self.quantity = quantity
        self.pricenakg = 500
        self.coffee_grinding_stage = coffee_grinding_stage
        self.price = self.pricenakg * self.quantity
        self.name = "Arabica Yellow Bourbon"


class Arabica_Jamaica_Blue_Mountain(Coffee):
    def __init__(self, quantity, coffee_grinding_stage, typepackaging):
        super().__init__(quantity, coffee_grinding_stage, typepackaging)
        self.quantity = quantity
        self.pricenakg = 4000
        self.coffee_grinding_stage = coffee_grinding_stage
        self.price = self.pricenakg * self.quantity
        self.name = "Arabica Jamaica Blue Mountain"

class Van:
    def __init__(self):
        self.max_kg = 100  # В кг и упаковках
        self.speendmoney = 0
        self.NameandQuality = dict()

    def load_up_the_Van(self, A):
        self.speendmoney += A.price
        self.max_kg -= A.quantity
        self.NameandQuality.update({int(A.pricenakg): str(A.name) + " (" + str(A.coffee_grinding_stage + ")")})

class Main:
    A = Arabica_Yellow_Bourbon(5, "Beans Coffee", "Coffee in Bags")
    B = Arabica_Jamaica_Blue_Mountain(6.5, "Beans Coffee", "Coffee in Bags")
    Mashina = Van()
    Mashina.load_up_the_Van(A)
    Mashina.load_up_the_Van(B)

    TipisonColection(Mashina)
