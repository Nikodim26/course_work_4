from abc import ABC, abstractmethod


class APIAdapter(ABC):
    """Шаблон для классов, работающих с api"""
    def __init__(self) -> None:
        self.url = None

    @abstractmethod
    def obtaining_information(self):
        """Получает информацию из api"""
        pass
