# from goroda import gorodaList
import random

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

gorodaList = ['Абаза', 'Абакан', 'Абдулино', 'Алексеевка', 'Алушта',
              'Анадырь', 'Анапа', 'Аша']

gorodaUsed = []

print("___Ход компьютера___")
compCity = random.choice(gorodaList)
print(compCity)
gorodaUsed.append(compCity)
gorodaList.remove(compCity)

userCity = input("___Ход игрока___\n")

if userCity not in gorodaList and userCity not in gorodaUsed:
    print("Этого города не существует!")
elif userCity in gorodaUsed:
    print("Этот город уже был!")
elif userCity[0].lower() != compCity[-1]:
    print("Город не подходит!")
else:
    gorodaUsed.append(userCity)
    gorodaList.remove(userCity)

