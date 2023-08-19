# deklarujemy i inicjalizujemy zmienne
actYear = 2023
pythonYear = 1989

# obliczamy wiek Pythona
agePython = actYear - pythonYear

# pobieramy dane
name = input('Jak sie nazywasz? ')
age = int(input('Ile masz lat? '))

# instrukcja warunkowa
if age > agePython:
    print('Jesteś starszy ode mnie.')
elif age < agePython:
    print('Jesteś młodszy ode mnie.')
else:
    print('Masz tyle samo lat co ja.')

# if age > agePython:
#     print('Jesteś starszy ode mnie.')
#
# else:
#     print('Jesteś młodszy ode mnie.')

if __name__ == '__main__':
    # wyświetlamy komunikaty
    print("Witaj", name)
    print("Mów mi python, mam", agePython, "lat.")
