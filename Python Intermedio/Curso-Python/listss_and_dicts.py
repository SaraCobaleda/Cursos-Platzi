def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Sara", "lastname": "Cobaleda"}

    super_list = [
        {"firstname": "Sara", "lastname": "Cobaleda"},
        {"firstname": "Camila", "lastname": "Cruz"},
        {"firstname": "Andres", "lastname": "Garcia"},
        {"firstname": "Erika", "lastname": "Lopez"},
        {"firstname": "Jose", "lastname": "Martinez"},
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    for key in super_list:
        print(key) 


if __name__ == '__main__':
    run()