"""Inspired by R. Martins' \"Clean Code\""""

from abc import ABC, abstractmethod

# see all abstract interfaces below
class Button(ABC):
    """Abstract interface for buttons"""

    @abstractmethod
    def paint(self) -> str:
        pass

    @abstractmethod
    def set_author(self) -> str:
        pass


class Checkbox(ABC):
    """Abstract interface for checkboxes"""

    @abstractmethod
    def paint(self) -> str:
        pass

    @abstractmethod
    def set_author(self) -> str:
        pass


class AbstractFactory(ABC):
    """
    Abstract interface declaring set of methods returning abstract products
    """

    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


# see concrete buttons below
class WindowsButton(Button):
    def paint(self) -> str:
        return "We are buggy yet gamers love us"

    def set_author(self) -> str:
        return "Bill Gates, essentially"


class MacButton(Button):
    def paint(self) -> str:
        return "Aesthetics in details"

    def set_author(self) -> str:
        return "Steve Jobes is our father"


# see concrete checkboxes below
class WindowsCheckbox(Checkbox):
    def paint(self) -> str:
        return "Wait until we eat all your RAM"

    def set_author(self) -> str:
        return "We already know him..."


class MacCheckbox(Checkbox):
    def paint(self) -> str:
        return "That's for what we charge money"

    def set_author(self) -> str:
        return "That guy even cared about us ;)"


# set concrete factories below
class WindowsFactory(AbstractFactory):
    def create_button(self) -> WindowsButton:
        return WindowsButton()

    def create_checkbox(self) -> WindowsCheckbox:
        return WindowsCheckbox()


class MacFactory(AbstractFactory):
    def create_button(self) -> MacButton:
        return MacButton()

    def create_checkbox(self) -> MacCheckbox:
        return MacCheckbox()


# OK, but why do we need it?
def client_code(factory: AbstractFactory) -> None:
    """
    The client code works with factories and products only through abstract
    types: AbstractFactory and AbstractProduct. This lets you pass any factory
    or product subclass to the client code without breaking it.
    """

    client_button = factory.create_button()
    client_checkbox = factory.create_checkbox()

    print("Button-specific info:")
    print(f"\r{client_button.paint()}")
    print(f"\r{client_button.set_author()}\n")

    print("Checkbox-specific info:")
    print(f"\r{client_checkbox.paint()}")
    print(f"\r{client_checkbox.set_author()}")


if __name__ == "__main__":
    # client code can now work with any concrete factory easily
    print("TESTING WINDOWS-SPECIFIC FACTORY:")
    client_code(WindowsFactory())  # as easy as passing an argument

    print("TESTING MAC-SPECIFIC FACTORY:")
    client_code(MacFactory())
