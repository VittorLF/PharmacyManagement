import json
import os


class Database:

    def __init__(self, path = None) -> None:
        self.path = path

    @property
    def exist_file(self) -> bool:
        return os.path.exists(self.path)

    def exist_folder(self, folder) -> bool:
        if os.path.exists(folder):
            return True
        else:
            os.mkdir(folder)
            return False

    def write_database(self, data) -> None:
        with open(self.path, 'w') as database:
            database.write(json.dumps(data))

    @property
    def read_file(self) -> list:
        with open(self.path, 'r') as database:
            return json.loads(database.read())
