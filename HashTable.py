from SinglyLinkedList import SLinkedList


class HashTable_Chained:
    def __init__(self):
        self.hashTableSize = 30
        self.vector = [None] * self.hashTableSize

    def get_hash_func(self, date):
        return date % self.hashTableSize

    def insert_hash(self, date):
        hash_key = self.get_hash_func(date)
        if self.vector[hash_key] is None:
            print("Lista Criada e data Inserida")
            S_List = SLinkedList()
            S_List.insert_SLinkedList(date)
            self.vector[hash_key] = S_List
        else:
            print("Data inserida")
            self.vector[hash_key].insert_SLinkedList(date)

    def search_hash(self, date):
        hash_key = self.get_hash_func(date)
        if self.vector[hash_key] is None:
            return None
        else:
            return self.vector[hash_key]

    def delete_hash(self, date):
        hash_key = self.get_hash_func(date)
        if self.vector[hash_key].get_size():
            return None

class HashTable_Open_Address:

    def __init__(self):
        self.hashTableSize = 30
        self.vector = [None] * self.hashTableSize

    def get_hash_func(self, date, i):
        return (date % self.hashTableSize) + i

    def insert_hash(self, date):
        i = 0
        while i != self.hashTableSize:
            hash_key = self.get_hash_func(date, i)
            if hash_key >= self.hashTableSize:
                break
            if self.vector[hash_key] is None or self.vector[hash_key] == "Deleted":
                self.vector[hash_key] = date
                print("Data inserida")
                return hash_key
            else:
                i = i + 1
        print("HashTable OverFlow")

    def search_hash(self, date):
        i = 0
        while i != self.hashTableSize:
            hash_key = self.get_hash_func(date, i)
            if self.vector[hash_key] is None:
                break
            elif self.vector[hash_key] == date:
                print("Data foi encontrada")
                return hash_key
            else:
                i = i + 1
        print("Data não encontrada")
        return None

    def delete_hash(self, date):
        hash_to_delete = self.search_hash(date)
        if hash_to_delete is not None:
            self.vector[hash_to_delete] = "Deleted"

    def print_hash(self):
        print(self.vector)
