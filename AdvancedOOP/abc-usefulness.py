from abc import ABCMeta, abstractmethod


class Laptop(metaclass=ABCMeta):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def price(self):
        pass


class Dell(Laptop):
    def __init__(self, name):
        super().__init__(name)

    def price(self):
        return f"The price for {self.name} is $2400"


class Apple(Laptop):
    def __init__(self, name):
        super().__init__(name)

    def price(self):
        return f"The price for {self.name} is $3700"


# The usefulness of using abstractmethods is that you can easily
# know each class has a needed function.
laptops = [Dell("Dell XPS 15"), Apple("Apple Macbook Pro 2020")]

# This allows us to, say, iterate over the needed function:
for laptop in laptops:
    print(laptop.price())
