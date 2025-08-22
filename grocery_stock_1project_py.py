stock = {
    "maçã": 5,
    "banana": 3,
    "pera":1,
    "morango": 93
}

conversão = {
    1: "uma",
    5: "cinco",
    3: "três",
    93: "noventa e três"
}

print('Hoje temos maçã, banana, pera e morango.')
fruta = input("Qual dessas frutas procura? ")
x = int(stock[fruta])

if stock[fruta] > 1:
    print(f'Temos {conversão[x]} {fruta}s em stock')
else:
    print(f'Temos {conversão[x]} {fruta} em stock')
