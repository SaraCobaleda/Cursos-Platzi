def run():
    # my_dict = {}
    # for x in range(1, 101):
    #     if x%3:
    #         my_dict[x]=x**3
    # print(my_dict)

    # my_dict = {x: x**3 for x in range (1, 101) if x%3}
    # print(my_dict)

    my_dict = {x: x**0.5 for x in range (1, 1001)}
    print(my_dict)


if __name__ == '__main__':
    run()