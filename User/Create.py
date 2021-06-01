from .Database import Database


class Create(Database):
    def __init__(self, path):
        super().__init__(path)

        
    def add_user(self, user, password):
        """
        Add new user 
        """
        data = [{"user": user, "Password": password}]

        if self.exist_folder("data") and self.exist_file:
            users = self.read_file
            users.append(data[0])

            self.write_database(users)
            return users
        else:
            self.write_database(data)
            return data[0]
