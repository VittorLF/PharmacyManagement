from .Database import Database


class Update(Database):
    def __init__(self, path) -> None:
        super().__init__(path=path)
    
    def update_user(self,id, user, password):
        new_data = self.read_file[id]
        data = {"user": user, "Password": password}
        new_data.update(data)
        self.write_database(new_data)
    
