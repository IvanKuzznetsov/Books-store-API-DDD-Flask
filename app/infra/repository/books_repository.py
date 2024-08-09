from abc import ABC, abstractmethod
from domain.book import Book


class BookRepository(ABC):
    @abstractmethod
    def add(self, book: Book):
        pass

    @abstractmethod
    def get(self, id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def delete(self, id):
        pass

    @abstractmethod
    def update(self, book: Book):
        pass
