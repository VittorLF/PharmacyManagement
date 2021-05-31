from .Database import Database


class Delete(Database):
    def __init__(self, path) -> None:
        super().__init__(path=path)

    def delete_user(self, id):
        new_data = self.read_file.pop(id)
        self.write_database(new_data)

    def clear_database(self):
        data = self.read_file
        data.pop(len(data))
        self.write_database(data)
