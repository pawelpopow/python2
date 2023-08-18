# deklarujemy i inicjalizujemy zmienne
actYear = 2023
pythonYear = 1989

# obliczamy wiek Pythona
agePython = actYear - pythonYear

# pobieramy dane
name = input('Jak sie nazywasz? ')
age = int(input('Ile masz lat? '))

if __name__ == '__main__':
    # wyświetlamy komunikaty
    print("Witaj", name)
    print("Mów mi python, mam", agePython, "lat.")