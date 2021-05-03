from __future__ import annotations
from abc import ABC, abstractmethod


class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:

        product = self.factory_method()

        result = f"lorem15 {product.operation()}"

        return result


class ConcreteCreator1(Creator):


    def factory_method(self) -> Product:
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self) -> Product:
        return ConcreteProduct2()


class Product(ABC):

    @abstractmethod
    def operation(self) -> str:
        pass



class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "lorem10"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "lorem99"


def client_code(creator: Creator) -> None:

    print(f"lorem2\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("lorem53")
    client_code(ConcreteCreator1())
    print("\n")

    print("lorem22")
    client_code(ConcreteCreator2())