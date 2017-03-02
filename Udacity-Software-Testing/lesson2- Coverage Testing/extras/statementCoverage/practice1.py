def main(n):
    if n > 50:
        print n
    if n > 60:
        print n


def test():
    # 50% coverage
    main(50)
    # 89 %
    main(55)
    # 100
    main(100)
test()