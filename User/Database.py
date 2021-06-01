import json
import os


class Database:

    def __init__(self, path):
        self.path = path

    @property
    def exist_file(self):
        return os.path.exists(self.path)

    def exist_folder(self, folder):
        if os.path.exists(folder):
            return True
        else:
            os.mkdir(folder)
            return False

    def write_database(self, data):
        with open(self.path, 'w') as database:
            database.write(json.dumps(data))

    @property
    def read_file(self) -> list:
        with open(self.path, 'r') as database:
            return json.loads(database.read())
