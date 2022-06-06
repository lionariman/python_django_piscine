class Intern:
    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted."

    def __init__(self, name=None):
        if name is None:
            self.name = "My name? I'm nobody, an intern, I have no name."
            return
        self.name = name
    
    def __str__(self):
        return self.name

    def work(self):
        raise Exception("I'm just an intern, I can't do that...")

    def make_coffee(self):
        return self.Coffee


def main():
    nobody = Intern()
    mark = Intern("Mark")
    print("nobody.name: ", nobody)
    print("mark.name: ", mark)
    try:
        nobody.work()
    except Exception as e:
        print("Exception: ", e)
    coffee = mark.make_coffee()
    print(coffee())

if __name__ == "__main__":
    main()