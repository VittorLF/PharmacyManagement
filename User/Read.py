from .Database import Database


class Read(Database):
    def __init__(self, id: int):
        self.id = id

    def __search(self, users):
        if self.id <= len(users):
            return users[self.id]
        else:
            raise IndexError("user id not exist")

    def search_user(self):
        """
        Returns all user data
        """
        users = self.read_file
        return self.__search(users)
    