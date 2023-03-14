from abc import ABC, abstractmethod


class Youtube_class(ABC):
    """
    абстрактный класс для определения будущих методов
    """

    @abstractmethod
    def set_api_key(self):
        """метод класса для получения значения API ключа из config.py"""
        pass

    @abstractmethod
    def get_service(self):
        """метод класса для получения объекта build,
        через который осуществляется доступ к сервису youtube"""
        pass
