import random
from beverages import *

class CoffeeMachine:
    def __init__(self):
        self.count = 10

    class EmptyCup(HotBeverage):
        def __init__(self):
            self.name = "empty cup"
            self.price = 0.90

        def description(self):
            return "An empty cup? Gimme my money back!"

    class BrockenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired.")

    def repair(self):
        self.count = 10
    
    def serve(self, some_tasty_liquid: HotBeverage) -> HotBeverage():
        self.count -= 1
        if self.count <= 0:
            raise self.BrockenMachineException()
        if random.randint(0, 3) == 0:
            return self.EmptyCup()
        return some_tasty_liquid()



def main():
    coffe_machine = CoffeeMachine()
    for _ in range(25):
        try:
            print(
                coffe_machine.serve(random.choice([Coffee, Tea, Chocolate, Cappuccino]))
            )
        except CoffeeMachine.BrockenMachineException as e:
            print(e)
            coffe_machine.repair()

if __name__ == "__main__":
    main()