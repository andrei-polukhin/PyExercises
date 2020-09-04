from abc import ABCMeta, abstractmethod


class Equation(metaclass=ABCMeta):
    def __init__(self, equation):
        self.equation = equation

    @staticmethod
    def student_says():
        return "Oh, I love algebra!"

    @abstractmethod
    def roots(self):
        pass


class Linear(Equation):
    def __init__(self, equation):
        super().__init__(equation)

    def roots(self):
        return f"{self.equation} gives one root (as for a linear equation)"


# Specifying an object for Equation class is prohibited: it can only be used
# as a scaffold for building other classes.

# Specifying an object of Linear class is possible:
linear = Linear("3x-y+2=0")
print(linear.student_says())
print(linear.roots())

# Interestingly, if we specify the child class of Equation without the roots
# function, we will get an error as we use the decorator @abstractmethod
print("Now we will get an error!")


class Square(Equation):
    def __init__(self, equation):
        super().__init__(equation)


square = Square("x**2")
