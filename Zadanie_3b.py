number = int(input("Podaj liczbę: "))

def dividers( number ):
    dividers_list = []
    i = 1
    while i <= number // 2:
        if number % i == 0:
            dividers_list.append(i)
        i += 1
    if len(dividers_list) == 1:
        dividers_list.append(number)
    elif number == 1:
        dividers_list.append(1)
    return (dividers_list)

print(f"Dzieliniki liczby {number} to: {dividers(number)}")
