
listing_0009 = list(range(0, 10))  # from 0000 to 0009
listing_0099 = list(range(10, 100))  # from 0010 to 0099
listing_0999 = list(range(100, 1000))  # from 0099 to 0999
listing_9999 = list(range(1000, 10000))  # from 0999 to 9999


def pin():

    # from 0000 to 0009
    for number in listing_0009:
        print("".join('000' + str(number)))

    # from 0010 to 0099
    for number in listing_0099:
        print("".join('00' + str(number)))

    # from 0099 to 0999
    for number in listing_0999:
        print("".join('0' + str(number)))

    # from 0999 to 9999
    for number in listing_9999:
        print(number)

pin()
