number = input("Podaj liczbę, której pierwiastek kwadratowy mam obliczyć: ")
rounding = input("Z jaką dokładnością ma być podany wynik: ")

def squerroot_round( number, rounding ):
    squerroot = number ** 0.5
    result = round(squerroot, rounding)
    return (result)

print(f"Wynik to: {squerroot_round(float(number),int(rounding))}")
