class HashTable:
    def __init__(self, size=7):
        self.size = size
        self.data_map = [None] * size

    def set_item(self, key, value):
        index = self.__hash(key)

        if self.data_map[index] is None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_value(self, key):
        index = self.__hash(key)

        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        keys = []

        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    keys.append(self.data_map[i][j][0])
        return keys

    def __hash(self, key):
        return hash(key) % self.size
