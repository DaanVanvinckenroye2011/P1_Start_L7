prijzenkast = ("knuffelbeer", "gameconsole", "fiets")

print("Welkom bij de prijzenkast van de tv-show!")
print("Achter één van de dozen staat een verrassing. Kies doos 1, 2 of 3 en ontdek wat je gewonnen hebt!")

print("1. Doos 1")
print("2. Doos 2")
print("3. Doos 3")

gekozennummer = input("Kies nu of nooit!!")

x = prijzenkast[int(gekozennummer)-1]
print(x)