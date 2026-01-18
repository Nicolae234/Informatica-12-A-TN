def dictionairy():
    key_value = {}
    key_value[2] = 10
    key_value[1] = 5
    key_value[5] = 30
    key_value[4] = 20
    key_value[6] = 25
    key_value[3] = 15

    print("key_value", key_value)

    for i in sorted(key_value.keys()):
        print(key_value[i], end=" ")
    print()

    for i in sorted(key_value.keys()):
        print(i, end=" ")
    print()


def dictionairy2():
    key_value = {}
    key_value[2] = 10
    key_value[1] = 5
    key_value[5] = 30
    key_value[4] = 20
    key_value[6] = 25
    key_value[3] = 15

    print("key_value", key_value)

    items = [(v, k) for k, v in key_value.items()]

    items_sorted = sorted(items)

    for v, k in items_sorted:
        print(v, end=" ")
    print()

def dictionairy3():
    key_value = {}
    key_value[2] = 10
    key_value[1] = 5
    key_value[5] = 30
    key_value[4] = 20
    key_value[6] = 25
    key_value[3] = 15

    print("key_value", key_value)

    print("Sortat după cheie:")
    for i in sorted(key_value.keys()):
        print(key_value[i], end=" ")
    print()

    print("Sortat după valoare:")

    items = [(v, k) for k, v in key_value.items()]
    items_sorted = sorted(items)

    for v, k in items_sorted:
        print((k, v), end=" ")
    print()

def main():
    dictionairy()
    dictionairy2()
    dictionairy3()

if __name__ == "__main__":
    main()
