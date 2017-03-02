def main(x, y):
    z = x + 2 * y
    if z > 50:
        print z


def test():
    # test1
    main(2,3)
    # test2
    main(0,25)
    # test 3
    main(47,1)

    # this cover 100%
    main(20, 25)
test()