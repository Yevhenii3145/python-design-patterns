"""Мост — это структурный паттерн, который разделяет бизнес-логику или большой класс
на несколько отдельных иерархий, которые потом можно развивать отдельно друг от друга."""
from __future__ import annotations
from abc import ABC, abstractmethod


class Abstraction:
    def __init__(self, implementation: Implementation) -> None:
        self.implementation = implementation

    def operation(self) -> str:
        return (f"Abstraction: Base operation with: \n"
                f"{self.implementation.operation_implementation()}")


class ExtendedAbstracion(Abstraction):
    def operation(self) -> str:
        return (f"ExtendedAbstraction: Extended operation with:\n"
                f"{self.implementation.operation_implementation()}")


class Implementation(ABC):
    @abstractmethod
    def operation_implementation(self) -> str:
        pass


class ConcreteImplementationA(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationA: Here's the result on the platform A."


class ConcreteImplementationB(Implementation):
    def operation_implementation(self) -> str:
        return "ConcreteImplementationB: Here's the result on the platform B."


def client_code(abstraction: Abstraction) -> None:
    print(abstraction.operation(), end="")


if __name__ == "__main__":
    implementation = ConcreteImplementationA()
    abstraction = Abstraction(implementation)
    # Abstraction: Base operation with:
    # ConcreteImplementationA: Here's the result on the platform A.
    client_code(abstraction)

    print("\n")

    impolementation = ConcreteImplementationB()
    abstraction = ExtendedAbstracion(implementation)
    # ExtendedAbstraction: Extended operation with:
    # ConcreteImplementationA: Here's the result on the platform A.
    client_code(abstraction)
