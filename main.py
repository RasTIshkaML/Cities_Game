from goroda import gorodaList
import random

def find_last_letter(word):
    char = word[-2] if word[-1] in ["ь", "ы"] else word[-1]
    return char

print("""░░░│
░░╔╧╗
░╔╝▀╚╗
░╟▀─▀╢
░╟▀─▀╢
╔╩▀─▀╩╗┌█▀█─┐
╟▀─▀─▀╚█▀█▀█┴┐╔╗╔═╗
╟▀─▀─▀ГОРОДА▀█▀┴╜╟╢▀╚╗╔╗
╟▀─▀─▀─█▀█▀▀─▀┌╨╨▀┐╟╢║
╨▀─▀─▀─▀─▀─▀─▀┴▀─▀┴╨╨╨┈""")

# gorodaList = ['Абаза', 'Абакан', 'Абдулино', 'Алексеевка', 'Алушта',
#               'Анадырь', 'Анапа', 'Аша']

gorodaUsed = []

Game = True

print("___Ход компьютера___")
compCity = random.choice(gorodaList)
compCity = 'Казань'
lastLetter = find_last_letter(compCity)
print(compCity)
gorodaUsed.append(compCity)
gorodaList.remove(compCity)


while Game:
    # --------сделать так, чтобы пользователь вводил города до тех пор, пока не введет верный----
    while True:
        userCity = input("___Ход игрока___\n")

        if userCity == "стоп":
            Game = False
            break

        elif userCity not in gorodaList and userCity not in gorodaUsed:
            print("Этого города не существует!")
        elif userCity in gorodaUsed:
            print("Этот город уже был!")
        elif userCity[0].lower() != lastLetter:
            print("Город не подходит!")
        else:
            gorodaUsed.append(userCity)
            gorodaList.remove(userCity)
            lastLetter = find_last_letter(userCity)
            break

    if Game:
        print("___Ход компьютера___")
        for compCity in gorodaList:
            if compCity[0].lower() == lastLetter:
                print(compCity)
                gorodaUsed.append(compCity)
                gorodaList.remove(compCity)
                lastLetter = find_last_letter(compCity)
                break

        else:
            print('Компьютер Проиграл')
            Game = False