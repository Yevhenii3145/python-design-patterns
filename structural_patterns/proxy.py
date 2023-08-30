"""Заместитель — это объект, который выступает прослойкой между клиентом
и реальным сервисным объектом. Заместитель получает вызовы
от клиента, выполняет свою функцию (контроль доступа, кеширование,
изменение запроса и прочее), а затем передаёт вызов сервисному объекту."""
from abc import ABC, abstractmethod


class Subject(ABC):
    @abstractmethod
    def request(self) -> None:
        pass


class RealSubject(Subject):
    def request(self) -> None:
        print("RealSubject: Handling request.")


class Proxy(Subject):
    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def request(self) -> None:
        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self) -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self) -> None:
        print("Proxy: Logging the time of request.", end="")


def client_code(subject: Subject) -> None:
    subject.request()


if __name__ == "__main__":
    print("Client: Executing the client code with a real subject:")
    real_subject = RealSubject()
    # RealSubject: Handling request.
    client_code(real_subject)

    print("")

    print("Client: Executing the same client code with a proxy:")
    proxy = Proxy(real_subject)
    # Proxy: Checking access prior to firing a real request.
    # RealSubject: Handling request.
    # Proxy: Logging the time of request.
    client_code(proxy)
