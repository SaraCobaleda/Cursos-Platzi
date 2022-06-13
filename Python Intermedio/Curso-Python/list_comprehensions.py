def run():
    # squares = []
    # for x in range(1, 101):
    #     if x%3:
    #         squares.append(x**2)

    # squares = [x**2 for x in range(1, 101) if x % 3]
    # for key in squares:
    #     print(key)

    multiple_num = [x for x in range(1, 1000) if x%36==0]
    for key in multiple_num:
        print(key)


if __name__ == '__main__':
    run()