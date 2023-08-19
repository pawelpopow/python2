op = "t"
while op == "t":
    a, b, c = input("Podaj trzy liczby oddzielone spacjami: ").split(" ")

    print("Wprowadzono liczby:", a, b, c)
    print("\nNajmniejsza:")

    if a < b:
        if a < c:
            smallest = a
        else:
            smallest = c
    elif b < c:
        smallest = b
    else:
        smallest = c

        print(smallest)

        op = input("Jeszcze raz (t/n)? ")
if __name__ == '__main__':
    print("Koniec.")