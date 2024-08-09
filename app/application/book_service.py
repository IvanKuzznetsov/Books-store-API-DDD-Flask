class BookService:
    def __init__(self, storage):
        self.storage = storage

    def add(self, book):
        return self.storage.add(book)

    def get_all(self):
        return self.storage.get_all()

    def get(self, id):
        return self.storage.get(id)

    def update(self, book):
        return self.storage.update(book)

    def delete(self, id):
        return self.storage.delete(id)

