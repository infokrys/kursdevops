def duplicates(text):
    dict = {}
    dup = 0
    # inicjalizuje
    for x in text:
        dict[x] = 0

    # licze
    for x in text:
        dict[x] += 1

    # zwracam te sa zdublowane
    for x in dict:
        dup += dict[x] - 1

    return dup


print(duplicates("Hello World!"))
duplicates("foobar")
print(duplicates("helicopter"))
print(duplicates("birthday"))
