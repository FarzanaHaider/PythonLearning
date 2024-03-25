class Animal:

    Alive = True

    def eat(self):
        print("This animal eats")

    def sleep(self):
        print("This animal sleeps")

class bird(Animal):
    def fly(self):
        print("Bird can fly")

class rabbit(Animal):
    def run(self):
        print("Rabbit can run")

bunny = rabbit()
hawk = bird()

bunny.run()
hawk.fly()

