import operations


def main():
    print("{0:5d}".format(
        int(operations.addition(10, 5)),
    ))
    print("{0:5d}".format(
        int(operations.multiplication(8, 4))
    ))


if __name__ == "__main__":
    main()
