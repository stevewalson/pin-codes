
listing_000009 = list(range(0, 10))  # from 000000 to 000009
listing_000099 = list(range(10, 100))  # from 000010 to 000099
listing_000999 = list(range(100, 1000))  # from 000099 to 000999
listing_009999 = list(range(1000, 10000))  # from 000999 to 009999
listing_099999 = list(range(10000, 100000))  # from 009999 to 099999
listing_999999 = list(range(100000, 1000000))  # from 099999 to 999999


def pin():

    # from 000000 to 000009
    for number in listing_000009:
        print("".join('00000' + str(number)))

    # from 000010 to 000099
    for number in listing_000099:
        print("".join('0000' + str(number)))

    # from 000099 to 000999

    for number in listing_000999:
        print("".join('000' + str(number)))

    # from 000999 to 009999

    for number in listing_009999:
        print("".join('00' + str(number)))

    # from 009999 to 099999

    for number in listing_099999:
        print("".join('0' + str(number)))

    # from 099999 to 999999

    for number in listing_999999:
        print(number)

pin()
