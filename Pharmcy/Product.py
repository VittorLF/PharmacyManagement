from os import error, name
from .Database import Database


class Product(Database):
    def __init__(self, path):
        super().__init__(path)

    def __search_index(self, name):
        """
        Return index from product

        name: str
        """
        for index in range(len(self.read_file)):
            if name in self.read_file[index]:
                return index + 1
        return 0

    def add_product(self, name, data):
        """
        Add new product in database 

        name: str
        data: dict: {stuck, amount}

        """
        product_data = [
            {name: {"stuck": data["stuck"], "amount":data["amount"],"name":name}}]

        if self.exist_folder("data") and self.exist_file:
            if self.__search_index(name) <= 1:
                users = self.read_file
                users.append(product_data[0])
                self.write_database(users)

                return users[-1]

            else:
                raise IndexError("Product exist")

        else:
            self.write_database(product_data)
            return product_data[0]

    def update_product(self, name, data):
        """
        Update product data

        name: str
        data: dict: {stuck, amount}
        """
        old_data = self.read_file
        index = self.__search_index(name)
        if index:
            old_data[index-1][name]["stuck"] = data["stuck"]
            old_data[index-1][name]["amount"] = data["amount"]
            old_data[index-1][name]["name"] = name

            self.write_database(old_data)
            
            return old_data[index-1][name]
        else:
            return False

    def search_product(self, name):
        """
        Returns index the user 

        name: str
        """
        result = self.__search_index(name)
        return self.read_file[result-1][name]

    def delete_product(self, name):
        """
        Remove product from database and return true if successful

        user: str
        """
        new_data = self.read_file
        index = self.__search(name)

        if index:
            new_data.pop(index-1)
            self.write_database(new_data)
            return True
