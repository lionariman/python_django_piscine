class HotBeverage:
    def __init__(self) -> None:
        self.price = 0.30
        self.name = "hot beverage"

    def description(self) -> str:
        return "Just some hot water in a cup."
    
    def __str__(self) -> str:
        TEMPLATE = ("name: {name}\n"
                    "price: {price}\n"
                    "description: {description}")
        return TEMPLATE.format(name=self.name,
                               price=self.price,
                               description=self.description())
class Coffee:
    name: "coffee"
    price: 0.40
    description: "A coffee, to stay awake."

class Tea:
    name: "tea"
    price: 0.30
    description: "Just some hot water in a cup."

class Chocolate:
    name: "chocolate"
    price: 0.50
    description: "Chocolate, sweet chocolate..."

class Cappuccino:
    name: "coffee"
    price: 0.45
    description: "Un po' di Italia nella sua tazza!"

def main():


if __name__ == "__main__":
    main()        