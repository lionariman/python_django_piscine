class HotBeverage:
    def __init__(self) -> None:
        self.price = 0.30
        self.name = "hot beverage"

    def description(self) -> str:
        return "Just some hot water in a cup."
    
    def __str__(self) -> str:
        tmp = ("name: {name}\n"
                    "price: {price}\n"
                    "description: {description}")
        return tmp.format(name=self.name,
                               price=self.price,
                               description=self.description())
class Coffee(HotBeverage):
    def __init__(self) -> None:
        self.price = 0.40
        self.name = "coffee"
    
    def description(self) -> str:
        return "A coffee, to stay awake."

class Tea(HotBeverage):
    def __init__(self) -> None:
        self.price = 0.30
        self.name = "tea"
    
    def description(self) -> str:
        return "Just some hot water in a cup."

class Chocolate(HotBeverage):
    def __init__(self) -> None:
        self.price = 0.50
        self.name = "chocolate"

    def description(self) -> str:
        return "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
    def __init__(self) -> None:
        self.price = 0.45
        self.name = "coffee"

    def description(self) -> str:
        return "Un po' di Italia nella sua tazza!"

# def main():
#     print(HotBeverage())
#     print(Coffee())
#     print(Tea())
#     print(Chocolate())
#     print(Cappuccino())

# if __name__ == "__main__":
#     main()        