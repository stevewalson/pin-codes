
listing_00009 = list(range(0, 10))  # from 00000 to 00009
listing_00099 = list(range(10, 100))  # from 00010 to 00099
listing_00999 = list(range(100, 1000))  # from 00099 to 00999
listing_09999 = list(range(1000, 10000))  # from 00999 to 09999
listing_99999 = list(range(10000, 100000))  # from 00999 to 99999


def pin():
    # from 00000 to 00009
    for number in listing_00009:
        print("".join('0000' + str(number)))

    # from 00010 to 00099
    for number in listing_00099:
        print("".join('000' + str(number)))

    # from 00099 to 00999

    for number in listing_00999:
        print("".join('00' + str(number)))

    # from 00999 to 09999

    for number in listing_09999:
        print("".join('0' + str(number)))

    # from 09999 to 99999

    for number in listing_99999:
        print(number)

pin()
