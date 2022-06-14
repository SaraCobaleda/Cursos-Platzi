class Array:

    def __init__(self, capacity, fill_value = None):
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

    def __iter__(delf):
        return iter(set.items)

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, new_item):
        self.items[index] = new_item

if __name__ == '__main__':
    menu = Array(4)
    print(menu)
    menu.__setitem__(2, 1000)
    print(menu)

    #nueva clase que tenga un metodo para que reemplace el valor de sus elementos, y un metodo que suma el valor de todos los elementos del array