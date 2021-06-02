from .Database import Database


class User(Database):
    def __init__(self, path):
        super().__init__(path)

    def __search(self, name_user, password):
        """
        return index + 1

        name_user: str
        password:str
        """
        index = 0
        for user in self.read_file:
            index = + 1
            if user == {"user": name_user, "Password": password}:
                return index

    def add_user(self, user, password):
        """
        Add new user 

        user: str
        password: str
        """
        data = [{"user": user, "Password": password}]

        if self.exist_folder("data") and self.exist_file:
            users = self.read_file
            users.append(data[0])
            self.write_database(users)

            return users[-1]
        else:
            self.write_database(data)
            return data[0]

    def update_user(self, user, password, new_data):
        """
        Update user data

        user: str
        password: str
        new_data: dict
        """
        old_data = self.read_file
        index = self.__search(user, password)
        if index:
            old_data[index-1]["user"] = new_data["user"]
            old_data[index-1]["Password"] = new_data["Password"]
            self.write_database(old_data)
            return True
        else:
            return False

    def search_user(self, user, password):
        """
        Returns the user index
        
        user: str
        password: str
        """
        result = self.__search(user, password)
        return result

    def delete_user(self, user, password):
        """
        Remove user from database and return true if successful
        
        user: str
        password: str
        """
        new_data = self.read_file
        index = self.__search(user, password)
        if index:
            new_data.pop(index-1)
            self.write_database(new_data)
            return True

            