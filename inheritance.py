class Animal:
    def __init__(self):
        self.number_of_eyes = 2

    def breathe(self):
        print(True)

    def living(self):
        print("Living")


class Fish(Animal):
    def __init__(self):
        super().__init__()
        self.location = "water"

    def living(self):
        super().living()
        print("Living on Land")

    def swim(self):
        self.swims = True
        print(True)


nemo = Fish()

nemo.swim()
nemo.breathe()
nemo.living()
print(nemo.location)
print(nemo.number_of_eyes)